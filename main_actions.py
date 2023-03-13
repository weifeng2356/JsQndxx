#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import os

# 参数为 Cookie 里的 laravel_session, 请自行抓包获取
laravel_session = os.environ['LARAVEL_SESSION']


def get_latest_lesson(s, laravel_session):
    url = "https://service.jiangsugqt.org/api/cjdList"  # 江苏省青年大学习成绩单接口
    # 参数
    params = {
        "page": "1",
        "limit": "20"
    }
    # 构造请求头
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 13; 22127RK46C Build/TKQ1.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 XWEB/5015 MMWEBSDK/20230202 MMWEBID/3840 MicroMessenger/8.0.33.2320(0x2800213D) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        'Cookie': "laravel_session=" + laravel_session
    }
    res = s.post(url=url, headers=headers, params=params)  # 发送请求
    res = res.json()  # 返回结果转json
    if res["status"] == 1 and res["message"] == "操作成功":
        return res["data"][0]
    else:
        return None


def learn_lesson(s, laravel_session, lesson_id):
    url = "https://service.jiangsugqt.org/api/doLesson"  # 江苏省青年大学习接口
    # 参数
    params = {
        "lesson_id": lesson_id
    }
    # 构造请求头
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 13; 22127RK46C Build/TKQ1.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 XWEB/5015 MMWEBSDK/20230202 MMWEBID/3840 MicroMessenger/8.0.33.2320(0x2800213D) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        'Cookie': "laravel_session=" + laravel_session
    }
    res = s.post(url=url, headers=headers, params=params)  # 发送请求
    res = res.json()  # 返回结果转json
    print("%s: %s" % (lesson_id, res))
    if res["status"] == 1 and res["message"] == "操作成功":
        pass
    else:
        print("学习失败")


def main(laravel_session):
    s = requests.session()  # 创建会话
    latest_lesson = get_latest_lesson(s, laravel_session)
    if laravel_session == None:
        print("无法查询成绩单，请检查 Cookie 是否正确")
        return
    if latest_lesson["has_learn"] == '1':
        print("本周的 %s 已经学过了" % latest_lesson["title"])
        return

    learn_lesson(s, laravel_session, latest_lesson["id"])


if __name__ == '__main__':
    main(laravel_session)
