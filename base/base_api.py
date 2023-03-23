# -*- coding: utf-8 -*-
"""
Time   : 2022/11/18 18:13
Author : daiao
"""

from api.sys_login import BaseToken
from base.base_config import BaseConfig


class BaseApi:
    def __init__(self):
        self.token = BaseToken()
        self.base_config = BaseConfig()

    @property
    def login_token(self):
        """全局token"""
        return {
            "token": self.token.login_token
        }
