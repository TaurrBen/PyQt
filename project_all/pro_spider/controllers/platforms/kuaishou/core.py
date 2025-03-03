# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：  
# 1. 不得用于任何商业用途。  
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。  
# 3. 不得进行大规模爬取或对平台造成运营干扰。  
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。   
# 5. 不得用于任何非法或不当的用途。
#   
# 详细许可条款请参阅项目根目录下的LICENSE文件。  
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。  

# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : core.py
# Time       ：2025.2.27 0:06
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""

import asyncio
import time
from asyncio import Task

from PyQt5.QtCore import QCoreApplication
from playwright.async_api import (async_playwright, Playwright)

from utils.qEvent import ViewDataEvent
from utils.spider import *
from project_all.pro_spider.models.platforms.kuaishou import store as kuaishou_store
from project_all.pro_spider.models.var import crawler_type_var, source_keyword_var,comment_tasks_var

from .client import KuaiShouClient
from .exception import DataFetchError
from .login import KuaishouLogin


class KuaishouCrawler(AbstractCrawler):
    playwright: Playwright = None
    browser_context: BrowserContext
    context_page: Page
    ks_client: KuaiShouClient

    def __init__(self,parent = None):
        self.parent = parent
        self.index_url = "https://www.kuaishou.com"
        self.user_agent = get_user_agent()
        self.params = {}

    def load_params(self,params:Dict):
        self.params = params
        config.logger.info(self.params)

    async def search_by_keyword(self):
        config.logger.info("[KuaishouCrawler.search] Begin search kuaishou keywords")
        ks_limit_count = 20  # kuaishou limit page fixed value
        if config.CRAWLER_MAX_NOTES_COUNT < ks_limit_count:
            config.CRAWLER_MAX_NOTES_COUNT = ks_limit_count
        start_page = config.START_PAGE
        for keyword in config.KEYWORDS.split(","):
            source_keyword_var.set(keyword)
            config.logger.info(f"[KuaishouCrawler.search] Current search keyword: {keyword}")
            page = 1
            while (page - start_page + 1) * ks_limit_count <= config.CRAWLER_MAX_NOTES_COUNT:
                if page < start_page:
                    config.logger.info(f"[KuaishouCrawler.search] Skip page: {page}")
                    page += 1
                    continue
                config.logger.info(f"[KuaishouCrawler.search] search kuaishou keyword: {keyword}, page: {page}")
                video_id_list: List[str] = []
                videos_res = await self.ks_client.search_info_by_keyword(
                    keyword=keyword,
                    pcursor=str(page),
                )
                if not videos_res:
                    config.logger.error(f"[KuaishouCrawler.search] search info by keyword:{keyword} not found data")
                    continue

                vision_search_photo: Dict = videos_res.get("visionSearchPhoto")
                if vision_search_photo.get("result") != 1:
                    config.logger.error(f"[KuaishouCrawler.search] search info by keyword:{keyword} not found data ")
                    continue

                for video_detail in vision_search_photo.get("feeds"):
                    video_id_list.append(video_detail.get("photo", {}).get("id"))
                    await kuaishou_store.update_kuaishou_video(video_item=video_detail)

                # batch fetch video comments
                page += 1
                await self.batch_get_video_comments(video_id_list)
        config.logger.info("[KuaishouCrawler.start] Kuaishou CrawlerApi finished ...")
    async def start(self):
        if self.playwright:
            await self.context_page.close()
            await self.browser_context.close()
            await self.playwright.stop()

        playwright_proxy_format, httpx_proxy_format = None, None
        if config.ENABLE_IP_PROXY:
            ip_proxy_pool = await create_ip_pool(config.IP_PROXY_POOL_COUNT, enable_validate_ip=True)
            ip_proxy_info: IpInfoModel = await ip_proxy_pool.get_proxy()
            playwright_proxy_format, httpx_proxy_format = self.format_proxy_info(ip_proxy_info)

        self.playwright = Playwright(await async_playwright().start())
        # async with async_playwright() as playwright:
        if True:
            # Launch a browser context.
            self.browser_context = await self.launch_browser(
                self.playwright.chromium,
                None,
                self.user_agent,
                headless=self.params.get("headless")
            )
            # stealth.min.js is a js script to prevent the website from detecting the crawler.
            await self.browser_context.add_init_script(path="libs/stealth.min.js")
            self.context_page = await self.browser_context.new_page()
            await self.context_page.goto(f"{self.index_url}?isHome=1")

            # Create a client to interact with the kuaishou website.
            self.ks_client = await self.create_ks_client(httpx_proxy_format)
            if not await self.ks_client.pong():
                login_obj = KuaishouLogin(
                    login_type=config.LOGIN_TYPE,
                    login_phone="",
                    browser_context=self.browser_context,
                    context_page=self.context_page,
                    cookie_str=config.COOKIES
                )
                await login_obj.begin(config.LOGIN_TYPE)
                await self.ks_client.update_cookies(browser_context=self.browser_context)

            crawler_type_var.set(config.CRAWLER_TYPE)
            config.logger.info("[KilibiliCrawler.start] Kuaishou CrawlerApi Ready ...")
            event = ViewDataEvent("textBrowser_context", None, self.ks_client.headers,
                                  "for key,value in event.data.items():qwidget.append(f'{key}:{value}')")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("textBrowser_cookies", None, self.ks_client.cookie_dict,
                                  "for key,value in event.data.items():qwidget.append(f'{key}:{value}')")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_start_search", None, None,
                                  "qwidget.setEnabled(True)")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_stop_search", None, None,
                                  "qwidget.setEnabled(False)")
            QCoreApplication.postEvent(self.parent.ui, event)
            # if config.CRAWLER_TYPE == "search":
            #     # Search for videos and retrieve their comment information.
            #     await self.search()
            # elif config.CRAWLER_TYPE == "detail":
            #     # Get the information and comments of the specified post
            #     await self.get_specified_videos()
            # elif config.CRAWLER_TYPE == "creator":
            #     # Get creator's information and their videos and comments
            #     await self.get_creators_and_videos()
            # else:
            #     pass

    async def stop(self):
        if self.playwright:
            await self.context_page.close()
            await self.browser_context.close()
            await self.playwright.stop()
        event = ViewDataEvent("pushButton_load_params", None, None,
                              "qwidget.setEnabled(True)")
        QCoreApplication.postEvent(self.parent.ui, event)
        event = ViewDataEvent("pushButton_start_search", None, None,
                              "qwidget.setEnabled(False)")
        QCoreApplication.postEvent(self.parent.ui, event)
        event = ViewDataEvent("pushButton_stop_search", None, None,
                              "qwidget.setEnabled(False)")
        QCoreApplication.postEvent(self.parent.ui, event)

    async def search(self):
        config.logger.info("[KuaishouCrawler.search] Begin search kuaishou keywords")
        ks_limit_count = 20  # kuaishou limit page fixed value
        if config.CRAWLER_MAX_NOTES_COUNT < ks_limit_count:
            config.CRAWLER_MAX_NOTES_COUNT = ks_limit_count
        start_page = config.START_PAGE
        for keyword in config.KEYWORDS.split(","):
            source_keyword_var.set(keyword)
            config.logger.info(f"[KuaishouCrawler.search] Current search keyword: {keyword}")
            page = 1
            while (page - start_page + 1) * ks_limit_count <= config.CRAWLER_MAX_NOTES_COUNT:
                if page < start_page:
                    config.logger.info(f"[KuaishouCrawler.search] Skip page: {page}")
                    page += 1
                    continue
                config.logger.info(f"[KuaishouCrawler.search] search kuaishou keyword: {keyword}, page: {page}")
                video_id_list: List[str] = []
                videos_res = await self.ks_client.search_info_by_keyword(
                    keyword=keyword,
                    pcursor=str(page),
                )
                if not videos_res:
                    config.logger.error(f"[KuaishouCrawler.search] search info by keyword:{keyword} not found data")
                    continue

                vision_search_photo: Dict = videos_res.get("visionSearchPhoto")
                if vision_search_photo.get("result") != 1:
                    config.logger.error(f"[KuaishouCrawler.search] search info by keyword:{keyword} not found data ")
                    continue

                for video_detail in vision_search_photo.get("feeds"):
                    video_id_list.append(video_detail.get("photo", {}).get("id"))
                    await kuaishou_store.update_kuaishou_video(video_item=video_detail)

                # batch fetch video comments
                page += 1
                await self.batch_get_video_comments(video_id_list)

    async def get_specified_videos(self):
        """Get the information and comments of the specified post"""
        semaphore = asyncio.Semaphore(config.MAX_CONCURRENCY_NUM)
        task_list = [
            self.get_video_info_task(video_id=video_id, semaphore=semaphore) for video_id in config.KS_SPECIFIED_ID_LIST
        ]
        video_details = await asyncio.gather(*task_list)
        for video_detail in video_details:
            if video_detail is not None:
                await kuaishou_store.update_kuaishou_video(video_detail)
        await self.batch_get_video_comments(config.KS_SPECIFIED_ID_LIST)

    async def get_video_info_task(self, video_id: str, semaphore: asyncio.Semaphore) -> Optional[Dict]:
        """Get video detail task"""
        async with semaphore:
            try:
                result = await self.ks_client.get_video_info(video_id)
                config.logger.info(f"[KuaishouCrawler.get_video_info_task] Get video_id:{video_id} info result: {result} ...")
                return result.get("visionVideoDetail")
            except DataFetchError as ex:
                config.logger.error(f"[KuaishouCrawler.get_video_info_task] Get video detail error: {ex}")
                return None
            except KeyError as ex:
                config.logger.error(f"[KuaishouCrawler.get_video_info_task] have not fund video detail video_id:{video_id}, err: {ex}")
                return None

    async def batch_get_video_comments(self, video_id_list: List[str]):
        """
        batch get video comments
        :param video_id_list:
        :return:
        """
        if not config.ENABLE_GET_COMMENTS:
            config.logger.info(f"[KuaishouCrawler.batch_get_video_comments] Crawling comment mode is not enabled")
            return

        config.logger.info(f"[KuaishouCrawler.batch_get_video_comments] video ids:{video_id_list}")
        semaphore = asyncio.Semaphore(config.MAX_CONCURRENCY_NUM)
        task_list: List[Task] = []
        for video_id in video_id_list:
            task = asyncio.create_task(self.get_comments(video_id, semaphore), name=video_id)
            task_list.append(task)

        comment_tasks_var.set(task_list)
        await asyncio.gather(*task_list)

    async def get_comments(self, video_id: str, semaphore: asyncio.Semaphore):
        """
        get comment for video id
        :param video_id:
        :param semaphore:
        :return:
        """
        async with semaphore:
            try:
                config.logger.info(f"[KuaishouCrawler.get_comments] begin get video_id: {video_id} comments ...")
                await self.ks_client.get_video_all_comments(
                    photo_id=video_id,
                    crawl_interval=random.random(),
                    callback=kuaishou_store.batch_update_ks_video_comments,
                    max_count=config.CRAWLER_MAX_COMMENTS_COUNT_SINGLENOTES
                )
            except DataFetchError as ex:
                config.logger.error(f"[KuaishouCrawler.get_comments] get video_id: {video_id} comment error: {ex}")
            except Exception as e:
                config.logger.error(f"[KuaishouCrawler.get_comments] may be been blocked, err:{e}")
                # use time.sleeep block main coroutine instead of asyncio.sleep and cacel running comment task
                # maybe kuaishou block our request, we will take a nap and update the cookie again
                current_running_tasks = comment_tasks_var.get()
                for task in current_running_tasks:
                    task.cancel()
                time.sleep(20)
                await self.context_page.goto(f"{self.index_url}?isHome=1")
                await self.ks_client.update_cookies(browser_context=self.browser_context)

    @staticmethod
    def format_proxy_info(ip_proxy_info: IpInfoModel) -> Tuple[Optional[Dict], Optional[Dict]]:
        """format proxy info for playwright and httpx"""
        playwright_proxy = {
            "server": f"{ip_proxy_info.protocol}{ip_proxy_info.ip}:{ip_proxy_info.port}",
            "username": ip_proxy_info.user,
            "password": ip_proxy_info.password,
        }
        httpx_proxy = {
            f"{ip_proxy_info.protocol}": f"http://{ip_proxy_info.user}:{ip_proxy_info.password}@{ip_proxy_info.ip}:{ip_proxy_info.port}"
        }
        return playwright_proxy, httpx_proxy

    async def create_ks_client(self, httpx_proxy: Optional[str]) -> KuaiShouClient:
        """Create ks client"""
        config.logger.info("[KuaishouCrawler.create_ks_client] Begin create kuaishou API client ...")
        cookie_str, cookie_dict = convert_cookies(await self.browser_context.cookies())
        ks_client_obj = KuaiShouClient(
            proxies=httpx_proxy,
            headers={
                "User-Agent": self.user_agent,
                "Cookie": cookie_str,
                "Origin": self.index_url,
                "Referer": self.index_url,
                "Content-Type": "application/json;charset=UTF-8"
            },
            playwright_page=self.context_page,
            cookie_dict=cookie_dict,
        )
        return ks_client_obj

    async def launch_browser(
            self,
            chromium: BrowserType,
            playwright_proxy: Optional[Dict],
            user_agent: Optional[str],
            headless: bool = True
    ) -> BrowserContext:
        """Launch browser and create browser context"""
        config.logger.info("[KuaishouCrawler.launch_browser] Begin create browser context ...")
        if config.SAVE_LOGIN_STATE:
            user_data_dir = os.path.join(os.getcwd(), "data/spider/browser_data",
                                         config.USER_DATA_DIR % "kuaishou")  # type: ignore
            browser_context = await chromium.launch_persistent_context(
                channel="chrome",
                user_data_dir=user_data_dir,
                accept_downloads=True,
                headless=headless,
                proxy=playwright_proxy,  # type: ignore
                viewport={"width": 1920, "height": 1080},
                user_agent=user_agent
            )
            return browser_context
        else:
            browser = await chromium.launch(
                channel="chrome",
                headless=headless,
                proxy=playwright_proxy)  # type: ignore
            browser_context = await browser.new_context(
                viewport={"width": 1920, "height": 1080},
                user_agent=user_agent
            )
            return browser_context

    async def get_creators_and_videos(self) -> None:
        """Get creator's videos and retrieve their comment information."""
        config.logger.info("[KuaiShouCrawler.get_creators_and_videos] Begin get kuaishou creators")
        for user_id in config.KS_CREATOR_ID_LIST:
            # get creator detail info from web html content
            createor_info: Dict = await self.ks_client.get_creator_info(user_id=user_id)
            if createor_info:
                await kuaishou_store.save_creator(user_id, creator=createor_info)

            # Get all video information of the creator
            all_video_list = await self.ks_client.get_all_videos_by_creator(
                user_id = user_id,
                crawl_interval = random.random(),
                callback = self.fetch_creator_video_detail
            )

            video_ids = [video_item.get("photo", {}).get("id") for video_item in all_video_list]
            await self.batch_get_video_comments(video_ids)

    async def fetch_creator_video_detail(self, video_list: List[Dict]):
        """
        Concurrently obtain the specified post list and save the data
        """
        semaphore = asyncio.Semaphore(config.MAX_CONCURRENCY_NUM)
        task_list = [
            self.get_video_info_task(post_item.get("photo", {}).get("id"), semaphore) for post_item in video_list
        ]

        video_details = await asyncio.gather(*task_list)
        for video_detail in video_details:
            if video_detail is not None:
                await kuaishou_store.update_kuaishou_video(video_detail)

    async def close(self):
        """Close browser context"""
        await self.browser_context.close()
        config.logger.info("[KuaishouCrawler.close] Browser context closed ...")
