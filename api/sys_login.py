# -*- coding: utf-8 -*-
"""
Time   : 2022/11/18 18:13
Author : daiao
"""
import os

import requests
import yaml

from base.base_singleton import BaseSingleton
from common import environment

config_file = os.path.join(environment.PATH, 'config', f"{environment.Environment}.yaml")


def file_reading(case):
    with open(config_file, 'r', encoding='UTF-8') as fs:
        data = yaml.load(fs, Loader=yaml.FullLoader)
        config = data.get(case)
        return config


class SysLogin:
    """登录客户端"""
    __url = "sys/login"

    def __init__(self):
        """账号/密码"""
        self.mobile = file_reading('mobile')
        self.password = file_reading('password')
        """运行环境配置"""
        self.test_url = file_reading('test_url')

    def sys_login(self):
        login_url = f'{self.test_url}{self.__url}'

        json_body = {
            "mobile": self.mobile,
            "password": self.password
        }

        resp = requests.post(login_url, json=json_body)
        data = resp.json()
        token = data['token']
        print(login_url)
        print(data)
        print(token)
        assert data['code'] == 0
        return token


class BaseToken(metaclass=BaseSingleton):
    def __init__(self):
        self.login_token = SysLogin().sys_login()
