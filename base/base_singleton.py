# -*- coding: utf-8 -*-
"""
Time   : 2022/11/18 18:13
Author : daiao
"""


class BaseSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)

        return cls._instance[cls]
