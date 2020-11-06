#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : BranchLogin_yame_case.py
# Author: tian guang yuan
# Time  : 2020/11/5 15:13
import yaml
import json
def get_yaml_data():
    yamlDir = '../data/Branch_yaml_test.yaml'
    fo = open(yamlDir, 'r', encoding="utf8")
    res = yaml.load(fo, Loader=yaml.FullLoader)
    # 封装数据
    resList = []
    for one in res:
        resList.append((json.dumps(one['detail']).encode('utf-8').decode('unicode_escape'), json.dumps(one['data']), json.dumps(one['check']).encode('utf-8').decode('unicode_escape')))
    return resList

if __name__ == '__main__':
    # indata, ser = get_yaml_data()[0]
    # print(json.loads(ser)['code'])
    print(get_yaml_data())











