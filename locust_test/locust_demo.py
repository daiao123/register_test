# -*- coding: utf-8 -*-
"""
Time   : 2023/1/17 9:41
Author : daiao
"""
from faker import Faker
from locust import HttpUser, TaskSet, task, between


class TaskTest(TaskSet):
    token = None
    idcard_image = "*"

    # def __init__(self):
    #     super(TaskTest, self).__init__()
    #     faker = Faker(locale='zh_CN')
    #     self.name = faker.name()
    #     self.phone = faker.phone_number()
    #     self.idcardId = faker.ssn()

    @task
    def login(self):
        url = '*'
        json = {
            "mobile": "*",
            "password": "*",
        }
        # header = {"Content-Type": "application/json;charset=UTF-8"}
        data = self.client.request(method='POST', url=url, json=json, name='登录')
        TaskTest.token = data.json()['token']
        # print(data.json())
        print(TaskTest.token)

    @task
    def donator_baseinfo_save(self):
        faker = Faker(locale='zh_CN')
        name = faker.name()
        phone = faker.phone_number()
        idcardId = faker.ssn()
        url = "*"

        json_body = {
            "idcardImage": self.idcard_image,
            "name": name,
            "sex": "男",
            "nation": "汉族",
            "birthday": "1988-09-21",
            "idcardId": idcardId,
            "idcardValiddate": "2009-12-18-2029-12-18",
            "issuedOrganization": "四川省简阳市石盘镇来宾路15号",
            "idcardAddress": "四川省简阳市石盘镇来宾路15号",
            "phone": phone,
            "employeeId": "",
            "profession": "",
            "township": "石盘镇",
            "homeAddress": "四川省简阳市石盘镇来宾路15号",
            "diseasehistory": "",
            "remark": "",
            "headimage": self.idcard_image,
            "idcardFrontBackImage": "*"
        }

        tokens = {
            "token": self.token
        }
        data = self.client.request(method='POST', url=url, json=json_body, headers=tokens, name='注册')
        print(data.json())
        print(idcardId)


class Login(HttpUser):
    host = '*'
    # wait_time = constant(3)  # 每次请求停顿时间 （思考时间）
    wait_time = between(1, 3)
    tasks = [TaskTest]

