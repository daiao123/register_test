from random import choice
from math import fabs
from datetime import date, datetime


def get_num8(x):
    """ 随机生成8位数 """
    if x == 17:
        return "%d" % (fabs(x) * choice(range(10 ** 8, 10 ** 9)))
    else:
        return "%d" % (x * choice(range(10 ** 8, 10 ** 9)))


def get_locations():
    """ 随机生成城市编号 """
    address = ['110101', '110102', '110103', '110104', '110105', '110106', '110107', '110108', '110109', '110111',
               '110112', '110113', '110114', '110115', '110116', '110117']
    return choice(address)


def get_birthday(x, startyear=1965):
    """ 随机生成yyyymmdd格式的日期 """
    start = date(startyear, 1, 1).toordinal()
    end = date.today().toordinal()

    o = date.fromordinal(choice(range(start, end)))
    return o.strftime("%Y%m%d")


def get_randnum(x):
    """ 随机生成3位数字 """
    if x == 17:
        return "%d" % (fabs(x) * choice(range(10 ** 3, 10 ** 4)))
    else:
        return "%d" % (x * choice(range(10 ** 3, 10 ** 4)))


def create_idcard(x, startyear=1965):
    """ 
    生成一个被接受的身份证号码 
    """
    new_idcard = get_locations()
    new_idcard += get_birthday(x, startyear)
    new_idcard += get_randnum(x)
    new_idcard += get_num8(x)

    i = 0
    counts = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                 '10': '2'}
    for a in new_idcard:
        i += int(a) * counts[i]
    if checkcode[str(i % 11)] == '5':
        new_idcard += '5'
    else:
        new_idcard += checkcode[str(i % 11)]

    return new_idcard


print(create_idcard(1))
