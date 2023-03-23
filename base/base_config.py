# -*- coding: utf-8 -*-
"""
Time   : 2022/12/30 13:52
Author : daiao
"""
from faker import Faker

from api.sys_login import file_reading
from base.base_singleton import BaseSingleton


class BaseConfig(metaclass=BaseSingleton):

    def __init__(self):
        """献浆员idcardImage"""
        self.idcard_image = file_reading('idcard_image')
        """运行环境配置"""
        self.test_url = file_reading('test_url')
        """faker随机数"""
        faker = Faker(locale='zh_CN')
        self.name = faker.name()
        self.phone = faker.phone_number()
        self.idcardId = faker.ssn()

        print(
            "运行环境: %s" % self.test_url + "\n" +
            "name: %s" % self.name + "\n" +
            "phone: %s" % self.phone + "\n" +
            "idcardid: %s" % self.idcardId + "\n" +
            "初始化配置完成。"
        )


# BaseConfig()
