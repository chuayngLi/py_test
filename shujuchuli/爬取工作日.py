# coding=utf-8
# !/usr/bin/python
import numpy as np
import requests
import json


# 从百度的php接口中获取到数据
def catch_url_from_baidu(calcultaion_year, month):
    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    param = {
        "query": calcultaion_year + "年" + month + "月",
        "resource_id": "39043",
        "t": "1604395059555",
        "ie": "utf8",
        "oe": "gbk",
        "format": "json",
        "tn": "wisetpl",
        "cb": ""
    }
    # 抓取位置：百度搜索框搜索日历，上面的日历的接口，可以在页面上进行核对
    r = requests.get(url="https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php",
                     headers=headers, params=param).text
    month_data = json.loads(r)["data"][0]["almanac"]
    not_work_day = []
    for one in month_data:
        # if one["cnDay"] == '日' or one["cnDay"] == '六':
        if one["cnDay"] == '一' or one["cnDay"] == '二' or one["cnDay"] == '三' or one["cnDay"] == '四' or one[
            "cnDay"] == '五':
            if 'status' in one:
                if one["status"] == "1":
                    # if one["status"] == "2":
                    # status为2的时候表示周末的工作日，比如10月10日。即百度工具左上角显示“班”的日期
                    continue
                else:
                    # 普通周末时间
                    not_work_day.append(one)
                    continue
            else:
                # 普通周末时间。（接口中，如果左上角没有特殊表示，则不会返回status）
                not_work_day.append(one)
                continue
        if 'status' in one and one["status"] == "2":
            # status为1的时候表示休息日，比如10月1日。即百度工具左上角显示“休”的日期
            not_work_day.append(one)
    # print_info(not_work_day)
    return not_work_day


def print_info(not_work_day):
    for one in not_work_day:
        if len(one['month']) < 2:
            one['month'] = '0' + one['month']
        if len(one['day']) < 2:
            one['day'] = '0' + one['day']
        # print(insert_sql)
    return not_work_day
    # print('|'.join(str(calcultaion_year + i["month"] + i["day"]) for i in not_work_day))
    # with open('./file/' + calcultaion_year, 'w') as f:
    #     f.write('|'.join(str(calcultaion_year + i["month"] + i["day"]) for i in not_work_day))
    # print(not_work_day)


if __name__ == '__main__':
    # 此处只能算当年之前的，因为国务院是每年12月份才会发布第二年的放假计划，所以此接口对于下一年的统计是错的。eg：2020年11月4日，国务院没有发布21年的放假计划，那查询2021年元旦的时候，元旦那天不显示休息
    calcultaion_year = "2022"
    # 因该接口传入的时间，查询了前一个月，当前月和后一个月的数据，所以只需要2、5、8、11即可全部获取到。比如查询5月份，则会查询4,5,6月分的数据
    calculation_month = ["2", "5", "8", "11"]
    # for one_month in calculation_month:
    #     catch_url_from_baidu(calcultaion_year, one_month)
    work_day = []
    for one_month in calculation_month:
        work_day.extend(catch_url_from_baidu(calcultaion_year, one_month))
        # print(catch_url_from_baidu(calcultaion_year, one_month))
    # print(np.append(work_day, []))
    arr = print_info(np.append(work_day, []))
    # print(arr)
    print('|'.join(str(calcultaion_year + i["month"] + i["day"]) for i in arr))
    with open('./file/' + calcultaion_year, 'w') as f:
        f.write('|'.join(str(calcultaion_year + i["month"] + i["day"]) for i in work_day))
