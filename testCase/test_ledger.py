#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : test_ledger.py
# Author: tian guang yuan
# Time  : 2020/11/4 17:31
import pytest
import json
import allure
from APILib.ApiLogin import LoginClass
from APILib.Total_Management import LedgerClass
from APILib.yame_case import get_yaml_data

@allure.step("步骤1:填写请求参数:inData,提交后返回实际结果")
def step_1():
    pass

@allure.step("步骤2:对比实际结果与预期结果:repsData")
def step_2():
    pass

@allure.feature("账套管理")  # 模块名称
class TestLesson:  # 测试用例类
    # 登录接口
    def setup_class(self):
        """课程模块——扥估初始化"""
        self.token = LoginClass().Total_Login()
    # 1.账套新增接口
    @allure.story('新增账套')
    @allure.title('账套添加')
    @pytest.mark.parametrize('inData,repsData', get_yaml_data())
    def test_add_ledger(self,inData,repsData):
        '''用例描述：账套新增接口'''
        step_1()
        res = LedgerClass().add_ledger(self.token, inData)
        step_2()
        assert int(res['code']) == json.loads(repsData)['code']





