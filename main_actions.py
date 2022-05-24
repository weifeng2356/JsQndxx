#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import requests
import urllib3
from bs4 import BeautifulSoup
import os

laravel_session = os.environ['LARAVEL_SESSION']

def main(laravel_session):  # 参数为cookie里的laravel_session 自行抓包获取
    s = requests.session()  # 创建会话
    loginurl = "https://service.jiangsugqt.org/youth/lesson"  # 江苏省青年大学习接口
    # 参数
    params = {
        "s": "/youth/lesson",
        "form": "inglemessage",
        "isappinstalled": "0"
    }
    # 构造请求头
    headers = {
        'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001234) NetType/WIFI Language/zh_CN",
        'Cookie': "laravel_session=" + laravel_session  # 抓包获取
    }
    urllib3.disable_warnings()  # 不然会有warning
    login = s.get(url=loginurl, headers=headers, params=params, verify=False)  # 登录

    login_soup = BeautifulSoup(login.text, 'html.parser')  # 解析信息确认页面
    userinfo = login_soup.select(".confirm-user-info p")  # 找到用户信息div 课程姓名编号单位

    dict = {}  # 构建用户信息字典

    for i in userinfo:
        info_soup = BeautifulSoup(str(i), 'html.parser')  # 分布解析课程姓名编号单位信息
        item = info_soup.get_text()  # 用户信息
        dict[item[:4]] = item[5:]
    token = re.findall(r'var token ?= ?"(.*?)"', login.text)  # 获取js里的token
    lesson_id = re.findall(r"'lesson_id':(.*)", login.text)  # 获取js里的token
    
    dict['token'] = token[0]
    dict['lesson_id'] = lesson_id[0]

    confirmurl = "https://service.jiangsugqt.org/youth/lesson/confirm"
    params = {
        "_token": token[0],
        "lesson_id": lesson_id[0]
    }
    res = s.post(url=confirmurl, params=params)
    res = res.json()  # 返回结果转json
    print("%s: %s" % (lesson_id[0], res))
    if res["status"] == 1 and res["message"] == "操作成功":
        pass
    else:
        print("error")

if __name__ == '__main__':
    main(laravel_session)