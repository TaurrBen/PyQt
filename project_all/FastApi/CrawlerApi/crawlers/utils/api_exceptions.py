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
# File       : api_exceptions.py
# Time       ：2025.3.3 16:50
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
class APIError(Exception):
    """基本API异常类，其他API异常都会继承这个类"""

    def __init__(self, status_code=None):
        self.status_code = status_code
        print(
            "程序出现异常，请检查错误信息。"
        )

    def display_error(self):
        """显示错误信息和状态码（如果有的话）"""
        return f"Error: {self.args[0]}." + (
            f" Status Code: {self.status_code}." if self.status_code else ""
        )


class APIConnectionError(APIError):
    """当与API的连接出现问题时抛出"""

    def display_error(self):
        return f"API Connection Error: {self.args[0]}."


class APIUnavailableError(APIError):
    """当API服务不可用时抛出，例如维护或超时"""

    def display_error(self):
        return f"API Unavailable Error: {self.args[0]}."


class APINotFoundError(APIError):
    """当API端点不存在时抛出"""

    def display_error(self):
        return f"API Not Found Error: {self.args[0]}."


class APIResponseError(APIError):
    """当API返回的响应与预期不符时抛出"""

    def display_error(self):
        return f"API Response Error: {self.args[0]}."


class APIRateLimitError(APIError):
    """当达到API的请求速率限制时抛出"""

    def display_error(self):
        return f"API Rate Limit Error: {self.args[0]}."


class APITimeoutError(APIError):
    """当API请求超时时抛出"""

    def display_error(self):
        return f"API Timeout Error: {self.args[0]}."


class APIUnauthorizedError(APIError):
    """当API请求由于授权失败而被拒绝时抛出"""

    def display_error(self):
        return f"API Unauthorized Error: {self.args[0]}."


class APIRetryExhaustedError(APIError):
    """当API请求重试次数用尽时抛出"""

    def display_error(self):
        return f"API Retry Exhausted Error: {self.args[0]}."