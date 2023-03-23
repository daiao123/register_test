# -*- coding: utf-8 -*-
"""
Time   : 2022/11/18 18:13
Author : daiao
"""
import requests

from base.base_api import BaseApi


class DonatorBaseinfoSave(BaseApi):
    """新浆员注册"""
    __url = "biz/donator/baseinfo/save"

    def donator_baseinfo_save(self):
        url = f"{self.base_config.test_url}{self.__url}"

        json_body = {
            "idcardImage": self.base_config.idcard_image,
            "name": self.base_config.name,
            "sex": "男",
            "nation": "汉族",
            "birthday": "1988-09-21",
            "idcardId": self.base_config.idcardId,
            "idcardValiddate": "2009-12-18-2029-12-18",
            "issuedOrganization": "四川省简阳市石盘镇来宾路15号",
            "idcardAddress": "四川省简阳市石盘镇来宾路15号",
            "phone": self.base_config.phone,
            "employeeId": "",
            "profession": "",
            "township": "石盘镇",
            "homeAddress": "四川省简阳市石盘镇来宾路15号",
            "diseasehistory": "",
            "remark": "",
            "headimage": self.base_config.idcard_image,
            "idcardFrontBackImage": "{\"frontaImage\":\"http://file.dev.uplasm.com/file/2022/11/16/20eacb918cba5b5b603801e051659f9c.png\",\"backImage\":\"http://file.dev.uplasm.com/file/2022/11/16/b600c9d7743e03df95dfc12e320091f0.png\"}"
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
