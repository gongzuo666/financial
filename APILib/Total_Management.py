#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : Total_Management.py
# Author: tian guang yuan
# Time  : 2020/11/4 13:46
from pprint import pprint
import requests
from config import Host
from APILib.ApiLogin import LoginClass
import json
class LedgerClass:
    # 1、新增账套
    def add_ledger(self, inToken, inData):
        token = inToken
        # 1、路径-url
        log_url = f'{Host}/qccw/ledger/insert'
        # 2、请求头信息
        header = {
                    'Content-Type': 'application/json',
                    'Authorization': f'{token}'
                }
        # 3、请求参数
        pay = inData
        payload = pay.encode("utf-8")
        reps = requests.post(log_url, data=payload, headers=header)
        return reps.json()

    # 2、账套列表
    def list_ledger(self, keyword):
        token = LoginClass().Total_Login()
        # 1、路径-url
        log_url = f'{Host}/qccw/ledger/list'
        # 2、请求头信息
        header = {
                    'Content-Type': 'application/json',
                    'Authorization': f'{token}'
                }
        # 3、请求参数
        pay = json.dumps({"keyword": keyword})
        payload = pay.encode("utf-8")
        reps = requests.post(log_url, data=payload, headers=header)
        return reps.json()["data"]["records"][0]["ledgerId"]
    #     resList = reps.json()["data"]["records"]
    #     # pprint(resList)
    #     while resList != []:
    #         for one in resList:
    #             ledgerId = one['ledgerId']
    #             print(ledgerId)
    #             LedgerClass().delete_ledger(ledgerId)
    #                 # return reps.json()
    #         resList = reps.json()["data"]["records"]
    # print('---------------------结束-------------------')


    def delete_ledger(self, ledgerId):
        token = LoginClass().Total_Login()
        # 1、路径-url
        log_url = f'{Host}/qccw/ledger/delete'
        # 2、请求头信息
        header = {
                    'Content-Type': 'application/json',
                    'Authorization': f'{token}',
                    'Host': '<calculated when request is sent>'
                }
        # 3、请求参数
        pay = json.dumps({"ledgerId": ledgerId, "type": "DELETE"})
        payload = pay.encode("utf-8")
        reps = requests.post(log_url, data=payload, headers=header)
        return reps.json()


if __name__ == '__main__':
    # 1、新增账套
    # aa = LedgerClass().add_ledger(
    #                                   '''{
    #                                   "packageName": "邢台公司",
    #                                   "createMouth": "202011",
    #                                   "loginAcc": "qwe",
    #                                   "loginPwd": "123456as",
    #                                   "confirmPwd": "123456as"
    #                                 }'''
    #                            )
    # print(aa)
    # 2、账套列表
    pprint(LedgerClass().list_ledger("青海1公司"))
    # 3、账套删除
    # pprint(delete_ledger("204"))









