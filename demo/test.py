# -*- coding: utf-8 -*-
"""
Time   : 2023/3/23 14:53
Author : daiao
"""

import random

# 参与抽奖的人员名单
names = ["第一个", "第二个", "第三个", "第四个", "第五个"]

# 抽出的人员数量
prize_num = 1

# 打印中奖名单
print("中奖名单：")

# 随机人员
for i in range(prize_num):
    # 从名单中随机选择一个名字
    winner = random.choice(names)

    # 打印中奖名单
    print(winner)

    # 从名单中删除已中奖的名字
    names.remove(winner)
