#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : yame_case.py
# Author: tian guang yuan
# Time  : 2020/11/4 16:58
import yaml
import json
def get_yaml_data():
    yamlDir = '../data/yeml_test.yaml'
    fo = open(yamlDir, 'r', encoding="utf8")
    res = yaml.load(fo, Loader=yaml.FullLoader)
    # 封装数据
    resList = []
    for one in res:
        resList.append((json.dumps(one['data']).encode('utf-8').decode('unicode_escape'), json.dumps(one['check'])))
    return resList

if __name__ == '__main__':
    # indata, ser = get_yaml_data()[1]
    # print(type(json.loads(ser)['code']))
    print(get_yaml_data())
