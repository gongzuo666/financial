#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : aa.py
# Author: tian guang yuan
# Time  : 2020/11/5 17:51
import pytest
import allure
# 作者：上海-悠悠 QQ交流群：779429633

def login(username, password):
    '''登录'''
    print("输入账号：%s" % username)
    print("输入密码：%s" % password)
    # 返回
    return {"code": 0, "msg": "success!"}


# 测试数据
test_datas = [
    ({"username": "yoyo1", "password": "123456"}, "success!", "输入正确账号，密码，登录成功"),
    ({"username": "yoyo2", "password": "123456"}, "failed!", "输入错误账号，密码，登录失败"),
    ({"username": "yoyo3", "password": "123456"}, "success!", "输入正确账号，密码，登录成功"),
]


@allure.story("登录用例")
@allure.title("{title}")
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas
                         )
def test_login(test_input, expected, title):
    '''测试登录用例'''
    # 获取函数返回结果
    result = login(test_input["username"], test_input["password"])
    # 断言
    assert result["msg"] == expected
