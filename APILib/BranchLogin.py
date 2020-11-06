#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : BranchLogin.py
# Author: tian guang yuan
# Time  : 2020/11/5 14:56
import requests
from config import Host
class LoginClass:
    def Total_Login(self, inData, gettoken = False):
        # 1、路径-url
        log_url = f'{Host}/qccw/user/login'
        # 2、请求头信息
        header = {
                    'Content-Type': 'application/json'
                  }
        # 3、请求参数
        payload = inData
        reps = requests.post(log_url, data=payload, headers=header)
        # 返回token信息
        # return reps.json()['data']['token']
        if gettoken:
            return reps.json()['data']['token']
        else:
            return reps.json()

if __name__ == '__main__':
    print(LoginClass().Total_Login('''{
                    "userType":"FINANCE",
                    "username":"",
                    "password":"e10adc3949ba59abbe56e057f20f883e",
                    "ledgerId":"194"
                }'''))




