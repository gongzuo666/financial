#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : test_login.py
# Author: tian guang yuan
# Time  : 2020/11/5 15:26
import pytest
import json
import allure
from APILib.BranchLogin import LoginClass
from APILib.BranchLogin_yame_case import get_yaml_data

'''
@allure.severity装饰器按严重性级别来标记case　　　
执行指定测试用例 --allure-severities blocker
BLOCKER = 'blocker'　　阻塞缺陷
CRITICAL = 'critical'　严重缺陷
NORMAL = 'normal'　　  一般缺陷
MINOR = 'minor'　　    次要缺陷
TRIVIAL = 'trivial'　　轻微缺陷　
'''

@allure.step("用例标题")
def step_1(detail):
    print(detail)

@allure.step("步骤1:填写请求参数:inData")
def step_2(inData):
    print(inData)

@allure.step("步骤2:对比实际结果:resdata与预期结果:repsData")
def step_3(resdata, repsData):
    print(resdata, repsData)

@allure.feature("登录")
class TestLesson:  # 测试用例类
    # 1.分公司登录
    @allure.story('分公司登录')
    @allure.title("{title}")
    @pytest.mark.parametrize('title,inData,expectData', get_yaml_data())
    def test_login(self,title,inData,expectData):
        '''
        用例描述：登录操作接口
        '''
        # step_1(detail)
        step_2(inData)
        actualData = LoginClass().Total_Login(inData)
        step_3(actualData, expectData)
        assert actualData['code'] == json.loads(expectData)['code']

    # @allure.severity("critical")
    # @allure.story("登录界面")
    # @allure.description("这里只是做一个web ui自动化的截图效果")
    # def test_login_image(self):
    #     allure.attach.file(r'../data/test.jpg', '我是附件截图的名字',
    #                        attachment_type=allure.attachment_type.JPG)


