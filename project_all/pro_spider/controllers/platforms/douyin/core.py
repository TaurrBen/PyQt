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
# Time       ：2025.2.26 22:50
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""

import asyncio
from asyncio import Task
from typing import Any

from PyQt5.QtCore import QCoreApplication
from playwright.async_api import (async_playwright, Playwright)

from utils.qEvent import ViewDataEvent
from utils.spider import *
from project_all.pro_spider.models.platforms.douyin import store as douyin_store
from project_all.pro_spider.models.var import crawler_type_var, source_keyword_var

from .client import DouyinClient
from .exception import DataFetchError
from .login import DouyinLogin


class DouyinCrawler(AbstractCrawler):
    playwright: Playwright = None
    browser_context: BrowserContext = None
    context_page: Page= None
    dy_client: DouyinClient= None

    def __init__(self,parent = None) -> None:
        self.parent = parent
        self.index_url = "https://www.douyin.com"
        self.params = {}

    def load_params(self, params:Dict):
        self.params = params
        config.logger.debug(self.params)

    async def start(self) -> None:
        if self.playwright:
            await self.context_page.close()
            await self.browser_context.close()
            await self.playwright.stop()
        config.logger.info("Douyin CrawlerApi Start ...")
        proxy_name = self.params.get("proxy")
        playwright_proxy_format, httpx_proxy_format = None, None
        if not proxy_name == "none":
            ip_proxy_pool = await create_ip_pool(config.IP_PROXY_POOL_COUNT, enable_validate_ip=True,proxy_name=proxy_name)
            ip_proxy_info: IpInfoModel = await ip_proxy_pool.get_proxy()
            playwright_proxy_format, httpx_proxy_format = self.format_proxy_info(ip_proxy_info)

        self.playwright = Playwright(await async_playwright().start())
        # async with async_playwright() as playwright:
        if True:
            # Launch a browser context.
            self.browser_context = await self.launch_browser(
                self.playwright.chromium,
                None,
                user_agent=None,
                headless=self.params.get("headless")
            )
            # stealth.min.js is a js script to prevent the website from detecting the crawler.
            await self.browser_context.add_init_script(path="libs/stealth.min.js")
            self.context_page = await self.browser_context.new_page()
            await self.context_page.goto(self.index_url)

            self.dy_client = await self.create_client(httpx_proxy_format)
            if not await self.dy_client.pong(browser_context=self.browser_context):
                login_obj = DouyinLogin(
                    login_type=self.params.get("login_type"),
                    login_phone="",  # you phone number
                    browser_context=self.browser_context,
                    context_page=self.context_page,
                    cookie_str=self.params.get("cookies"),
                )
                await login_obj.begin(self.params.get("login_type"))
                await self.dy_client.update_cookies(browser_context=self.browser_context)
            crawler_type_var.set(self.params.get("type"))
            config.logger.info("Douyin CrawlerApi Ready ...")
            event = ViewDataEvent("textBrowser_context", None, self.dy_client.headers,
                                  "for key,value in event.data.items():qwidget.append(f'{key}:{value}')")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("textBrowser_cookies", None, self.dy_client.cookie_dict,
                                  "for key,value in event.data.items():qwidget.append(f'{key}:{value}')")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_start_search", None, None,
                                  "qwidget.setEnabled(True)")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_stop_search", None, None,
                                  "qwidget.setEnabled(False)")
            QCoreApplication.postEvent(self.parent.ui, event)

    async def stop(self):
        if self.playwright:
            await self.context_page.close()
            await self.browser_context.close()
            await self.playwright.stop()
        config.logger.info("Douyin CrawlerApi Stop ...")
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
        type = self.params.get("type")
        if type == "keywords":
            await self.by_keywords(self.params.get("keywords"))
        elif type == "bvids":
            await self.by_aweme_ids(self.params.get("bvids"))
        elif type == "upuser":
            await self.by_creator(self.params.get("upuser"))
        else:
            config.logger.error(f"Have not {type}.")

    async def by_keywords(self,keywords):
        config.logger.info("Begin search douyin keywords")
        if self.params:
            dy_limit_count = 10  # douyin limit page fixed value
            if self.params.get("video_count") < dy_limit_count:
                self.params["video_count"] = dy_limit_count
            start_page = self.params.get("start_page") # start page number
            event = ViewDataEvent("pushButton_load_params", None, None,
                                  "qwidget.setEnabled(False)")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_start_search", None, None,
                                  "qwidget.setEnabled(False)")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_stop_search", None, None,
                                  "qwidget.setEnabled(True)")
            QCoreApplication.postEvent(self.parent.ui, event)

            for keyword in keywords:
                source_keyword_var.set(keyword)
                config.logger.info(f"Current keyword: {keyword}")
                aweme_list: List[str] = []
                page = 1
                dy_search_id = ""
                while (page - start_page + 1) * dy_limit_count <= self.params.get("video_count"):
                    if page < start_page:
                        config.logger.info(f"Skip {page}")
                        page += 1
                        continue
                    try:
                        config.logger.info(f"Search douyin keyword: {keyword}, page: {page}")
                        posts_res = await self.dy_client.search_general_by_keyword(
                            keyword=keyword,
                            offset=page * dy_limit_count - dy_limit_count,
                            sort_type="default",
                            publish_time="一周内",
                            filter_duration="default",
                            search_range="default",
                            content_type="default",
                            search_id=dy_search_id

                        )
                    except DataFetchError:
                        config.logger.error(f"Search douyin keyword: {keyword} failed")
                        break
                    page += 1
                    if "data" not in posts_res:
                        config.logger.error(
                            f"Search douyin keyword: {keyword} failed，账号也许被风控了。")
                        break
                    dy_search_id = posts_res.get("extra", {}).get("logid", "")
                    for post_item in posts_res.get("data"):
                        try:
                            aweme_info: Dict = post_item.get("aweme_info") or \
                                               post_item.get("aweme_mix_info", {}).get("mix_items")[0]
                        except TypeError:
                            continue
                        aweme_list.append(aweme_info.get("aweme_id", ""))
                        save_content_item = await douyin_store.update_douyin_aweme(
                            aweme_item=aweme_info,is_save=self.params.get("video_items_is_save"))
                        event = ViewDataEvent("self", None, list(save_content_item.values()),
                                              "self.tableWidget_video_items_addRow(event.data)")
                        QCoreApplication.postEvent(self.parent.ui, event)
                config.logger.info(f"Keyword:{keyword}, aweme_list:{aweme_list}")
                await self.batch_get_note_comments(aweme_list)
        config.logger.info("Douyin CrawlerApi finished ...")
        event = ViewDataEvent("pushButton_load_params", None, None,
                              "qwidget.setEnabled(True)")
        QCoreApplication.postEvent(self.parent.ui, event)
        event = ViewDataEvent("pushButton_start_search", None, None,
                              "qwidget.setEnabled(False)")
        QCoreApplication.postEvent(self.parent.ui, event)
        event = ViewDataEvent("pushButton_stop_search", None, None,
                              "qwidget.setEnabled(False)")
        QCoreApplication.postEvent(self.parent.ui, event)
        event = ViewDataEvent("pushButton_video_items_export", None, None,
                              "qwidget.setEnabled(True)")
        QCoreApplication.postEvent(self.parent.ui, event)
        event = ViewDataEvent("pushButton_video_upuser_items_export", None, None,
                              "qwidget.setEnabled(True)")
        QCoreApplication.postEvent(self.parent.ui, event)

    async def by_aweme_ids(self,aweme_ids):
        if self.params:
            event = ViewDataEvent("pushButton_load_params", None, None,
                                  "qwidget.setEnabled(False)")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_start_search", None, None,
                                  "qwidget.setEnabled(False)")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_stop_search", None, None,
                                  "qwidget.setEnabled(True)")
            QCoreApplication.postEvent(self.parent.ui, event)
            semaphore = asyncio.Semaphore(self.params.get("concurrency_num", 1))
            task_list = [
                self.get_aweme_by_id_task(aweme_id=aweme_id, semaphore=semaphore) for aweme_id in
                aweme_ids
            ]
            aweme_details = await asyncio.gather(*task_list)
            for aweme_detail in aweme_details:
                if aweme_detail is not None:
                    save_content_item = await douyin_store.update_douyin_aweme(
                        aweme_detail,self.params.get("video_items_is_save"))
                    event = ViewDataEvent("self", None, list(save_content_item.values()),
                                          "self.tableWidget_video_items_addRow(event.data)")
                    QCoreApplication.postEvent(self.parent.ui, event)
            await self.batch_get_aweme_comments(aweme_ids)
            config.logger.info("Douyin CrawlerApi finished ...")
            event = ViewDataEvent("pushButton_load_params", None, None,
                                  "qwidget.setEnabled(True)")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_start_search", None, None,
                                  "qwidget.setEnabled(False)")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_stop_search", None, None,
                                  "qwidget.setEnabled(False)")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_video_items_export", None, None,
                                  "qwidget.setEnabled(True)")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_video_upuser_items_export", None, None,
                                  "qwidget.setEnabled(True)")
            QCoreApplication.postEvent(self.parent.ui, event)

    async def by_creator(self,creator_id):
        if self.params:
            event = ViewDataEvent("pushButton_load_params", None, None,
                                  "qwidget.setEnabled(False)")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_start_search", None, None,
                                  "qwidget.setEnabled(False)")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_stop_search", None, None,
                                  "qwidget.setEnabled(True)")
            QCoreApplication.postEvent(self.parent.ui, event)
            config.logger.info("Begin get douyin creators")
            for user_id in creator_id:
                creator_info: Dict = await self.dy_client.get_user_info(user_id)
                if creator_info:
                    local_db_item = await douyin_store.save_creator(
                        user_id,creator=creator_info,is_save=self.params.get("video_upuser_items_is_save"))
                    event = ViewDataEvent("self", None, list(local_db_item.values()),
                                          "self.tableWidget_upuser_items_addRow(event.data)")
                    QCoreApplication.postEvent(self.parent.ui, event)
                # Get all video information of the creator
                all_video_list = await self.dy_client.get_all_user_aweme_posts(
                    sec_user_id=user_id,
                    callback=self.fetch_creator_video_detail
                )

                video_ids = [video_item.get("aweme_id") for video_item in all_video_list]
                await self.batch_get_aweme_comments(video_ids)
            config.logger.info("Douyin CrawlerApi finished ...")
            event = ViewDataEvent("pushButton_load_params", None, None,
                                  "qwidget.setEnabled(True)")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_start_search", None, None,
                                  "qwidget.setEnabled(False)")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_stop_search", None, None,
                                  "qwidget.setEnabled(False)")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_video_items_export", None, None,
                                  "qwidget.setEnabled(True)")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_video_upuser_items_export", None, None,
                                  "qwidget.setEnabled(True)")
            QCoreApplication.postEvent(self.parent.ui, event)
    #### aweme
    async def get_aweme_by_id_task(self, aweme_id: str, semaphore: asyncio.Semaphore) -> Any:
        """Get note detail"""
        async with semaphore:
            try:
                return await self.dy_client.get_aweme_by_id(aweme_id)
            except DataFetchError as ex:
                config.logger.error(f"Get aweme detail error: {ex}")
                return None
            except KeyError as ex:
                config.logger.error(f"have not fund note detail aweme_id:{aweme_id}, err: {ex}")
                return None

    #### aweme comment
    async def get_aweme_comments_task(self, aweme_id: str, semaphore: asyncio.Semaphore) -> None:
        async with semaphore:
            try:
                config.logger.info(f"Begin get video_id: {aweme_id} comments ...")
                # 将关键词列表传递给 get_aweme_all_comments 方法
                await self.dy_client.get_aweme_all_level_comments(
                    aweme_id=aweme_id,
                    crawl_interval=random.random(),
                    is_fetch_sub_comments=self.params.get("sub_comment"),
                    callback=douyin_store.batch_update_dy_aweme_comments,
                    max_count=self.params.get("comment_count"),
                )
                config.logger.info(
                    f"Aweme_id: {aweme_id} comments have all been obtained and filtered ...")
            except DataFetchError as e:
                config.logger.error(f"Aweme_id: {aweme_id} get comments failed, error: {e}")

    async def batch_get_aweme_comments(self, aweme_list: List[str]) -> None:
        """
        Batch get note comments
        """
        if not self.params.get("download_comment"):
            config.logger.info(f"Crawling comment mode is not enabled")
            return

        task_list: List[Task] = []
        semaphore = asyncio.Semaphore(self.params.get("concurrency_num",1))
        for aweme_id in aweme_list:
            task = asyncio.create_task(
                self.get_aweme_comments_task(aweme_id, semaphore), name=aweme_id)
            task_list.append(task)
        if len(task_list) > 0:
            await asyncio.wait(task_list)

    #### creator
    async def fetch_creator_video_detail(self, video_list: List[Dict]):
        """
        Concurrently obtain the specified post list and save the data
        """
        semaphore = asyncio.Semaphore(self.params.get("concurrency_num", 1))
        task_list = [
            self.get_aweme_by_id_task(post_item.get("aweme_id"), semaphore) for post_item in video_list
        ]

        note_details = await asyncio.gather(*task_list)
        for aweme_item in note_details:
            if aweme_item is not None:
                save_content_item = await douyin_store.update_douyin_aweme(
                    aweme_item,is_save=self.params.get("video_items_is_save"))
                event = ViewDataEvent("self", None, list(save_content_item.values()),
                                      "self.tableWidget_video_items_addRow(event.data)")
                QCoreApplication.postEvent(self.parent.ui, event)

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

    async def create_client(self, httpx_proxy: Optional[str]) -> DouyinClient:
        """Create douyin client"""
        cookie_str, cookie_dict = convert_cookies(await self.browser_context.cookies())  # type: ignore
        douyin_client = DouyinClient(
            proxies=httpx_proxy,
            headers={
                "User-Agent": await self.context_page.evaluate("() => navigator.userAgent"),
                "Cookie": cookie_str,
                "Host": "www.douyin.com",
                "Origin": "https://www.douyin.com/",
                "Referer": "https://www.douyin.com/",
                "Content-Type": "application/json;charset=UTF-8"
            },
            playwright_page=self.context_page,
            cookie_dict=cookie_dict,
        )
        return douyin_client

    async def launch_browser(
            self,
            chromium: BrowserType,
            playwright_proxy: Optional[Dict],
            user_agent: Optional[str],
            headless: bool = True
    ) -> BrowserContext:
        """Launch browser and create browser context"""
        config.logger.info("Begin create browser context ...")
        if self.params.get("is_save_login_state"):
            USER_DATA_DIR = "%s_user_data_dir"
            user_data_dir = os.path.join(os.getcwd(), "data/spider/browser_data",
                                         USER_DATA_DIR % "douyin")  # type: ignore
            browser_context = await chromium.launch_persistent_context(
                channel="chrome",
                user_data_dir=user_data_dir,
                accept_downloads=True,
                headless=headless,
                proxy=playwright_proxy,  # type: ignore
                viewport={"width": 1920, "height": 1080},
                user_agent=user_agent
            )  # type: ignore
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

    async def close(self) -> None:
        """Close browser context"""
        await self.browser_context.close()
        config.logger.info("Browser context closed ...")
