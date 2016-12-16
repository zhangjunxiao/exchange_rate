# c:\Python27\python.exe
# -*- coding: utf-8 -*-
import json,urllib
from urllib import urlencode


# ----------------------------------
# 汇率调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/80
# ----------------------------------

def main():
    # 配置您申请的APPKey
    appkey = "b9b043c5bfcd90dffa04d8d02e48e0fb"

    # 1.常用汇率查询
    request1(appkey, "GET")

    # 2.货币列表
    request2(appkey, "GET")

    # 3.实时汇率查询换算
    request3(appkey, "GET")


# 常用汇率查询
def request1(appkey, m="GET"):
    url = "http://op.juhe.cn/onebox/exchange/query"
    params = {
        "key": appkey,  # 应用APPKEY(应用详细页查询)

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"], res["reason"])
    else:
        print "request api error"


# 货币列表
def request2(appkey, m="GET"):
    url = "http://op.juhe.cn/onebox/exchange/list"
    params = {
        "key": appkey,  # 应用APPKEY(应用详细页查询)

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"], res["reason"])
    else:
        print "request api error"


# 实时汇率查询换算
def request3(appkey, m="GET"):
    url = "http://op.juhe.cn/onebox/exchange/currency"
    params = {
        "from": "CNY",  # 转换汇率前的货币代码
        "to": "USD",  # 转换汇率成的货币代码
        "key": appkey,  # 应用APPKEY(应用详细页查询)

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"], res["reason"])
    else:
        print "request api error"


if __name__ == '__main__':
    main()