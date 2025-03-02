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
# Time       ：2025.2.27 0:51
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""

from asyncio import Task

from PyQt5.QtCore import QCoreApplication
from playwright.async_api import Playwright

from project_all.pro_spider.models.platforms.tieba.store import *
from utils.qEvent import ViewDataEvent
from utils.spider import *
from project_all.pro_spider.models.platforms.tieba import store as tieba_store
from project_all.pro_spider.models.var import crawler_type_var, source_keyword_var

from .client import BaiduTieBaClient
from .field import SearchNoteType, SearchSortType
from .help import TieBaExtractor


class TiebaCrawler(AbstractCrawler):
    playwright: Playwright = None
    browser_context: BrowserContext = None
    context_page: Page = None
    tieba_client: BaiduTieBaClient = None

    def __init__(self,parent = None) -> None:
        self.parent = parent
        self.index_url = "https://tieba.baidu.com"
        self.user_agent = get_user_agent()
        self._page_extractor = TieBaExtractor()
        self.params = {}

    def load_params(self,params:Dict):
        self.params = params
        config.logger.info(self.params)

    async def search_by_keyword(self):
        config.logger.info("[BaiduTieBaCrawler.search] Begin search baidu tieba keywords")
        tieba_limit_count = 10  # tieba limit page fixed value
        if config.CRAWLER_MAX_NOTES_COUNT < tieba_limit_count:
            config.CRAWLER_MAX_NOTES_COUNT = tieba_limit_count
        start_page = config.START_PAGE
        for keyword in config.KEYWORDS.split(","):
            source_keyword_var.set(keyword)
            config.logger.info(f"[BaiduTieBaCrawler.search] Current search keyword: {keyword}")
            page = 1
            while (page - start_page + 1) * tieba_limit_count <= config.CRAWLER_MAX_NOTES_COUNT:
                if page < start_page:
                    config.logger.info(f"[BaiduTieBaCrawler.search] Skip page {page}")
                    page += 1
                    continue
                try:
                    config.logger.info(f"[BaiduTieBaCrawler.search] search tieba keyword: {keyword}, page: {page}")
                    notes_list: List[TiebaNote] = await self.tieba_client.get_notes_by_keyword(
                        keyword=keyword,
                        page=page,
                        page_size=tieba_limit_count,
                        sort=SearchSortType.TIME_DESC,
                        note_type=SearchNoteType.FIXED_THREAD
                    )
                    if not notes_list:
                        config.logger.info(f"[BaiduTieBaCrawler.search] Search note list is empty")
                        break
                    config.logger.info(f"[BaiduTieBaCrawler.search] Note list len: {len(notes_list)}")
                    await self.get_specified_notes(note_id_list=[note_detail.note_id for note_detail in notes_list])
                    page += 1
                except Exception as ex:
                    config.logger.error(
                        f"[BaiduTieBaCrawler.search] Search keywords error, current page: {page}, current keyword: {keyword}, err: {ex}")
                    break
        config.logger.info("[BaiduTieBaCrawler.start] Tieba Crawler finished ...")
    async def start(self) -> None:
        """
        Start the crawler
        Returns:

        """
        if self.playwright:
            await self.context_page.close()
            await self.browser_context.close()
            await self.playwright.stop()
        ip_proxy_pool, httpx_proxy_format = None, None
        if config.ENABLE_IP_PROXY:
            config.logger.info("[BaiduTieBaCrawler.start] Begin create ip proxy pool ...")
            ip_proxy_pool = await create_ip_pool(config.IP_PROXY_POOL_COUNT, enable_validate_ip=True)
            ip_proxy_info: IpInfoModel = await ip_proxy_pool.get_proxy()
            _, httpx_proxy_format = format_proxy_info(ip_proxy_info)
            config.logger.info(f"[BaiduTieBaCrawler.start] Init default ip proxy, value: {httpx_proxy_format}")

        # Create a client to interact with the baidutieba website.
        self.tieba_client = BaiduTieBaClient(
            ip_pool=ip_proxy_pool,
            default_ip_proxy=httpx_proxy_format,
        )
        crawler_type_var.set(config.CRAWLER_TYPE)
        config.logger.info("[BaiduTieBaCrawler.start] Tieba Crawler Ready ...")
        event = ViewDataEvent("textBrowser_context", None, self.tieba_client.headers,
                              "for key,value in event.data.items():qwidget.append(f'{key}:{value}')")
        QCoreApplication.postEvent(self.parent.ui, event)
        # event = ViewDataEvent("textBrowser_cookies", None, self.tieba_client.cookie_dict,
        #                       "for key,value in event.data.items():qwidget.append(f'{key}:{value}')")
        # QCoreApplication.postEvent(self.parent.ui, event)
        event = ViewDataEvent("pushButton_start_search", None, None,
                              "qwidget.setEnabled(True)")
        QCoreApplication.postEvent(self.parent.ui, event)
        event = ViewDataEvent("pushButton_stop_search", None, None,
                              "qwidget.setEnabled(False)")
        QCoreApplication.postEvent(self.parent.ui, event)
        # if config.CRAWLER_TYPE == "search":
        #     # Search for notes and retrieve their comment information.
        #     await self.search()
        #     await self.get_specified_tieba_notes()
        # elif config.CRAWLER_TYPE == "detail":
        #     # Get the information and comments of the specified post
        #     await self.get_specified_notes()
        # elif config.CRAWLER_TYPE == "creator":
        #     # Get creator's information and their notes and comments
        #     await self.get_creators_and_notes()
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

    async def search(self) -> None:
        """
        Search for notes and retrieve their comment information.
        Returns:

        """
        config.logger.info("[BaiduTieBaCrawler.search] Begin search baidu tieba keywords")
        tieba_limit_count = 10  # tieba limit page fixed value
        if config.CRAWLER_MAX_NOTES_COUNT < tieba_limit_count:
            config.CRAWLER_MAX_NOTES_COUNT = tieba_limit_count
        start_page = config.START_PAGE
        for keyword in config.KEYWORDS.split(","):
            source_keyword_var.set(keyword)
            config.logger.info(f"[BaiduTieBaCrawler.search] Current search keyword: {keyword}")
            page = 1
            while (page - start_page + 1) * tieba_limit_count <= config.CRAWLER_MAX_NOTES_COUNT:
                if page < start_page:
                    config.logger.info(f"[BaiduTieBaCrawler.search] Skip page {page}")
                    page += 1
                    continue
                try:
                    config.logger.info(f"[BaiduTieBaCrawler.search] search tieba keyword: {keyword}, page: {page}")
                    notes_list: List[TiebaNote] = await self.tieba_client.get_notes_by_keyword(
                        keyword=keyword,
                        page=page,
                        page_size=tieba_limit_count,
                        sort=SearchSortType.TIME_DESC,
                        note_type=SearchNoteType.FIXED_THREAD
                    )
                    if not notes_list:
                        config.logger.info(f"[BaiduTieBaCrawler.search] Search note list is empty")
                        break
                    config.logger.info(f"[BaiduTieBaCrawler.search] Note list len: {len(notes_list)}")
                    await self.get_specified_notes(note_id_list=[note_detail.note_id for note_detail in notes_list])
                    page += 1
                except Exception as ex:
                    config.logger.error(
                        f"[BaiduTieBaCrawler.search] Search keywords error, current page: {page}, current keyword: {keyword}, err: {ex}")
                    break

    async def get_specified_tieba_notes(self):
        """
        Get the information and comments of the specified post by tieba name
        Returns:

        """
        tieba_limit_count = 50
        if config.CRAWLER_MAX_NOTES_COUNT < tieba_limit_count:
            config.CRAWLER_MAX_NOTES_COUNT = tieba_limit_count
        for tieba_name in config.TIEBA_NAME_LIST:
            config.logger.info(
                f"[BaiduTieBaCrawler.get_specified_tieba_notes] Begin get tieba name: {tieba_name}")
            page_number = 0
            while page_number <= config.CRAWLER_MAX_NOTES_COUNT:
                note_list: List[TiebaNote] = await self.tieba_client.get_notes_by_tieba_name(
                    tieba_name=tieba_name,
                    page_num=page_number
                )
                if not note_list:
                    config.logger.info(
                        f"[BaiduTieBaCrawler.get_specified_tieba_notes] Get note list is empty")
                    break

                config.logger.info(
                    f"[BaiduTieBaCrawler.get_specified_tieba_notes] tieba name: {tieba_name} note list len: {len(note_list)}")
                await self.get_specified_notes([note.note_id for note in note_list])
                page_number += tieba_limit_count

    async def get_specified_notes(self, note_id_list: List[str] = config.TIEBA_SPECIFIED_ID_LIST):
        """
        Get the information and comments of the specified post
        Args:
            note_id_list:

        Returns:

        """
        semaphore = asyncio.Semaphore(config.MAX_CONCURRENCY_NUM)
        task_list = [
            self.get_note_detail_async_task(note_id=note_id, semaphore=semaphore) for note_id in note_id_list
        ]
        note_details = await asyncio.gather(*task_list)
        note_details_model: List[TiebaNote] = []
        for note_detail in note_details:
            if note_detail is not None:
                note_details_model.append(note_detail)
                await tieba_store.update_tieba_note(note_detail)
        await self.batch_get_note_comments(note_details_model)

    async def get_note_detail_async_task(self, note_id: str, semaphore: asyncio.Semaphore) -> Optional[TiebaNote]:
        """
        Get note detail
        Args:
            note_id: baidu tieba note id
            semaphore: asyncio semaphore

        Returns:

        """
        async with semaphore:
            try:
                config.logger.info(f"[BaiduTieBaCrawler.get_note_detail] Begin get note detail, note_id: {note_id}")
                note_detail: TiebaNote = await self.tieba_client.get_note_by_id(note_id)
                if not note_detail:
                    config.logger.error(
                        f"[BaiduTieBaCrawler.get_note_detail] Get note detail error, note_id: {note_id}")
                    return None
                return note_detail
            except Exception as ex:
                config.logger.error(f"[BaiduTieBaCrawler.get_note_detail] Get note detail error: {ex}")
                return None
            except KeyError as ex:
                config.logger.error(
                    f"[BaiduTieBaCrawler.get_note_detail] have not fund note detail note_id:{note_id}, err: {ex}")
                return None

    async def batch_get_note_comments(self, note_detail_list: List[TiebaNote]):
        """
        Batch get note comments
        Args:
            note_detail_list:

        Returns:

        """
        if not config.ENABLE_GET_COMMENTS:
            return

        semaphore = asyncio.Semaphore(config.MAX_CONCURRENCY_NUM)
        task_list: List[Task] = []
        for note_detail in note_detail_list:
            task = asyncio.create_task(self.get_comments_async_task(note_detail, semaphore), name=note_detail.note_id)
            task_list.append(task)
        await asyncio.gather(*task_list)

    async def get_comments_async_task(self, note_detail: TiebaNote, semaphore: asyncio.Semaphore):
        """
        Get comments async task
        Args:
            note_detail:
            semaphore:

        Returns:

        """
        async with semaphore:
            config.logger.info(f"[BaiduTieBaCrawler.get_comments] Begin get note id comments {note_detail.note_id}")
            await self.tieba_client.get_note_all_comments(
                note_detail=note_detail,
                crawl_interval=random.random(),
                callback=tieba_store.batch_update_tieba_note_comments,
                max_count=config.CRAWLER_MAX_COMMENTS_COUNT_SINGLENOTES
            )

    async def get_creators_and_notes(self) -> None:
        """
        Get creator's information and their notes and comments
        Returns:

        """
        config.logger.info("[WeiboCrawler.get_creators_and_notes] Begin get weibo creators")
        for creator_url in config.TIEBA_CREATOR_URL_LIST:
            creator_page_html_content = await self.tieba_client.get_creator_info_by_url(creator_url=creator_url)
            creator_info: TiebaCreator = self._page_extractor.extract_creator_info(creator_page_html_content)
            if creator_info:
                config.logger.info(f"[WeiboCrawler.get_creators_and_notes] creator info: {creator_info}")
                if not creator_info:
                    raise Exception("Get creator info error")

                await tieba_store.save_creator(user_info=creator_info)

                # Get all note information of the creator
                all_notes_list = await self.tieba_client.get_all_notes_by_creator_user_name(
                    user_name=creator_info.user_name,
                    crawl_interval=0,
                    callback=tieba_store.batch_update_tieba_notes,
                    max_note_count=config.CRAWLER_MAX_NOTES_COUNT,
                    creator_page_html_content=creator_page_html_content,
                )

                await self.batch_get_note_comments(all_notes_list)

            else:
                config.logger.error(
                    f"[WeiboCrawler.get_creators_and_notes] get creator info error, creator_url:{creator_url}")

    async def launch_browser(
            self,
            chromium: BrowserType,
            playwright_proxy: Optional[Dict],
            user_agent: Optional[str],
            headless: bool = True
    ) -> BrowserContext:
        """
        Launch browser and create browser
        Args:
            chromium:
            playwright_proxy:
            user_agent:
            headless:

        Returns:

        """
        config.logger.info("[BaiduTieBaCrawler.launch_browser] Begin create browser context ...")
        if config.SAVE_LOGIN_STATE:
            # feat issue #14
            # we will save login state to avoid login every time
            user_data_dir = os.path.join(os.getcwd(), "data/spider/browser_data",
                                         config.USER_DATA_DIR % tieba)  # type: ignore
            browser_context = await chromium.launch_persistent_context(
                user_data_dir=user_data_dir,
                accept_downloads=True,
                headless=headless,
                proxy=playwright_proxy,  # type: ignore
                viewport={"width": 1920, "height": 1080},
                user_agent=user_agent
            )
            return browser_context
        else:
            browser = await chromium.launch(headless=headless, proxy=playwright_proxy)  # type: ignore
            browser_context = await browser.new_context(
                viewport={"width": 1920, "height": 1080},
                user_agent=user_agent
            )
            return browser_context

    async def close(self):
        """
        Close browser context
        Returns:

        """
        await self.browser_context.close()
        config.logger.info("[BaiduTieBaCrawler.close] Browser context closed ...")
