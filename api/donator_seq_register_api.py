# -*- coding: utf-8 -*-
"""
Time   : 2022/12/1 13:44
Author : daiao
"""
import requests

from base.base_api import BaseApi


class DonatorSeqRegisterApi(BaseApi):
    """新浆员登记"""
    __url = "biz/donator/seq/register"

    def donator_seq_register_api(self):
        url = f"{self.base_config.test_url}{self.__url}"

        json_body = {
            "idcardId": self.base_config.idcardId,
            "recruitPromoterId": '',
            "registerType": 0
        }

        resp = requests.post(url, json=json_body, headers=self.login_token)
        print(url)
        print(json_body)
        print(resp.json())
        return resp.json()
