# -*- coding: utf-8 -*-
"""
Time   : 2022/11/18 18:13
Author : daiao
"""
import os

pwd = os.getcwd()

Environment = os.getenv('Environment')

PATH = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
