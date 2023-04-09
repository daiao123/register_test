# -*- coding: utf-8 -*-
"""
Time   : 2022/11/18 18:13
Author : daiao
"""
import requests

from base.base_api import BaseApi
from demo import generate_and_crack_ID_card


class DonatorBaseinfoSave(BaseApi):
    """新浆员注册"""
    __url = "biz/donor/register"
    idcardId = generate_and_crack_ID_card.idcardId

    def donator_baseinfo_save(self):
        url = f"{self.base_config.test_url}{self.__url}"

        json_body = {
            "idcardImage": self.base_config.idcard_image,
            "name": self.base_config.name,
            "gender": "FEMALE",
            "nation": "汉族",
            "idcardId": self.idcardId,
            "idcardValidDate": "2000-12-18-2027-12-18",
            "issuedOrganization": "四川省简阳市公安局",
            "idcardAddress": "四川省简阳市杨家镇大佛镇大堰坎酒店垭村2组",
            "phone": self.base_config.phone,
            "profession": "务农",
            "township": "",
            "remark": "",
            "frontPhoto": "*",
            "backPhoto": "*",
            "headImage": "*",
            "score": 0.91
        }
        resp = requests.post(url, json=json_body, headers=self.login_token)
        # print({
        #     "name: %s" % json_body['name'],
        #     "idcardId: %s" % json_body['idcardId']
        # })
        # print(json_body)
        print(url)
        print(resp.json())
        return resp.json()
