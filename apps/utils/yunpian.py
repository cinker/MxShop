#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 上午 09:54
# @Author  : gao
# @File    : yunpian.py
import json

import requests


class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【南工在线超市】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == "__main__":
    yun_pian = YunPian("70c240ba6c189c5ea639f99edbb70a49")
    yun_pian.send_sms("2018", "17633626710")