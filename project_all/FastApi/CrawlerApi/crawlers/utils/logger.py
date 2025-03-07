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
# File       : logger.py
# Time       ：2025.3.3 16:51
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
import threading
import time
import logging
import datetime

from pathlib import Path
from rich.logging import RichHandler
from logging.handlers import TimedRotatingFileHandler


class Singleton(type):
    _instances = {}  # 存储实例的字典
    _lock: threading.Lock = threading.Lock()  # 线程锁

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        """
        重写默认的类实例化方法。当尝试创建类的一个新实例时，此方法将被调用。
        如果已经有一个与参数匹配的实例存在，则返回该实例；否则创建一个新实例。
        """
        key = (cls, args, frozenset(kwargs.items()))
        with cls._lock:
            if key not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[key] = instance
        return cls._instances[key]

    @classmethod
    def reset_instance(cls, *args, **kwargs):
        """
        重置指定参数的实例。这只是从 _instances 字典中删除实例的引用，
        并不真正删除该实例。如果其他地方仍引用该实例，它仍然存在且可用。
        """
        key = (cls, args, frozenset(kwargs.items()))
        with cls._lock:
            if key in cls._instances:
                del cls._instances[key]


class LogManager(metaclass=Singleton):
    def __init__(self):
        if getattr(self, "_initialized", False):  # 防止重复初始化
            return

        self.logger = logging.getLogger("Douyin_TikTok_Download_API_Crawlers")
        self.logger.setLevel(logging.INFO)
        self.log_dir = None
        self._initialized = True

    def setup_logging(self, level=logging.INFO, log_to_console=False, log_path=None):
        self.logger.handlers.clear()
        self.logger.setLevel(level)

        if log_to_console:
            ch = RichHandler(
                show_time=False,
                show_path=False,
                markup=True,
                keywords=(RichHandler.KEYWORDS or []) + ["STREAM"],
                rich_tracebacks=True,
            )
            ch.setFormatter(logging.Formatter("{message}", style="{", datefmt="[%X]"))
            self.logger.addHandler(ch)

        if log_path:
            self.log_dir = Path(log_path)
            self.ensure_log_dir_exists(self.log_dir)
            log_file_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S.log")
            log_file = self.log_dir.joinpath(log_file_name)
            fh = TimedRotatingFileHandler(
                log_file, when="midnight", interval=1, backupCount=99, encoding="utf-8"
            )
            fh.setFormatter(
                logging.Formatter(
                    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                )
            )
            self.logger.addHandler(fh)

    @staticmethod
    def ensure_log_dir_exists(log_path: Path):
        log_path.mkdir(parents=True, exist_ok=True)

    def clean_logs(self, keep_last_n=10):
        """保留最近的n个日志文件并删除其他文件"""
        if not self.log_dir:
            return
        # self.shutdown()
        all_logs = sorted(self.log_dir.glob("*.log"))
        if keep_last_n == 0:
            files_to_delete = all_logs
        else:
            files_to_delete = all_logs[:-keep_last_n]
        for log_file in files_to_delete:
            try:
                log_file.unlink()
            except PermissionError:
                self.logger.warning(
                    f"无法删除日志文件 {log_file}, 它正被另一个进程使用"
                )

    def shutdown(self):
        for handler in self.logger.handlers:
            handler.close()
            self.logger.removeHandler(handler)
        self.logger.handlers.clear()
        time.sleep(1)  # 确保文件被释放


def log_setup(log_to_console=True):
    logger = logging.getLogger("Douyin_TikTok_Download_API_Crawlers")
    if logger.hasHandlers():
        # logger已经被设置，不做任何操作
        return logger

    # 创建临时的日志目录
    temp_log_dir = Path("./logs")
    temp_log_dir.mkdir(exist_ok=True)

    # 初始化日志管理器
    log_manager = LogManager()
    log_manager.setup_logging(
        level=logging.INFO, log_to_console=log_to_console, log_path=temp_log_dir
    )

    # 只保留1000个日志文件
    log_manager.clean_logs(1000)

    return logger


logger = log_setup()