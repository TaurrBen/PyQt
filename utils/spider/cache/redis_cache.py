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
# File       : redis_cache.py
# Time       ：2025.2.22 10:34
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
import os
import pickle
import time
from typing import Any, List

from redis import Redis

from .abs_cache import AbstractCache


class RedisCache(AbstractCache):

    def __init__(self,host,port,db,password) -> None:
        # 连接redis, 返回redis客户端
        self._redis_client = self._connet_redis(host,port,db,password)

    @staticmethod
    def _connet_redis(host,port,db,password) -> Redis:
        """
        连接redis, 返回redis客户端, 这里按需配置redis连接信息
        :return:
        host=db_config.REDIS_DB_HOST,
        port=db_config.REDIS_DB_PORT,
        db=db_config.REDIS_DB_NUM,
        password=db_config.REDIS_DB_PWD,
        """
        return Redis(host=host,port=port,db=db,password=password)

    def get(self, key: str) -> Any:
        """
        从缓存中获取键的值, 并且反序列化
        :param key:
        :return:
        """
        value = self._redis_client.get(key)
        if value is None:
            return None
        return pickle.loads(value)

    def set(self, key: str, value: Any, expire_time: int) -> None:
        """
        将键的值设置到缓存中, 并且序列化
        :param key:
        :param value:
        :param expire_time:
        :return:
        """
        self._redis_client.set(key, pickle.dumps(value), ex=expire_time)

    def keys(self, pattern: str) -> List[str]:
        """
        获取所有符合pattern的key
        """
        return [key.decode() for key in self._redis_client.keys(pattern)]


if __name__ == '__main__':
    host = "127.0.0.1"  # your redis host
    password = os.getenv("REDIS_DB_PWD", "123456")  # your redis password
    port = os.getenv("REDIS_DB_PORT", 6379)  # your redis port
    db = os.getenv("REDIS_DB_NUM", 0)
    redis_cache = RedisCache(host=host,port=port,db=db,password=password)
    # basic usage
    redis_cache.set("name", "程序员阿江-Relakkes", 1)
    print(redis_cache.get("name"))  # Relakkes
    print(redis_cache.keys("*"))  # ['name']
    time.sleep(2)
    print(redis_cache.get("name"))  # None

    # special python type usage
    # list
    redis_cache.set("list", [1, 2, 3], 10)
    _value = redis_cache.get("list")
    print(_value, f"value type:{type(_value)}")  # [1, 2, 3]