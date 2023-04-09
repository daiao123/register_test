# -*- coding: utf-8 -*-
"""
Time   : 2022/11/18 18:13
Author : daiao
"""

import allure

from api.donator_baseinfo_save import DonatorBaseinfoSave
from api.donator_seq_register_api import DonatorSeqRegisterApi


@allure.feature("主流程")
class TestSysLogin:

    @allure.title("注册")
    def test_donator_baseinfo_save(self):
        resp = DonatorBaseinfoSave().donator_baseinfo_save()
        assert resp['code'] == "0"

    @allure.title("登记")
    def test_donator_seq_register(self):
        resp = DonatorSeqRegisterApi().donator_seq_register_api()
        assert resp['code'] == 0
