# -*- coding: utf-8 -*-
"""
Time   : 2022/11/18 18:13
Author : daiao
"""

import requests

from base.base_api import BaseApi


class OfferplasmaLastData(BaseApi):
    """获取新浆员信息"""
    __url = "biz/donator/offerplasma/lastData?"

    def offerplasma_lastData_api(self):
        url = f"{self.base_config.test_url}{self.__url}"

        params_body = {
            "id": self.base_config.idcardId
        }

        resp = requests.get(url, params=params_body, headers=self.login_token)
        print(url)
        print(params_body)
        print(resp.json())
        return resp.json()


OfferplasmaLastData().offerplasma_lastData_api()
