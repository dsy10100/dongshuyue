# -*- coding: utf-8 -*-
"""
@author：dongdong
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestDepartment:
    main = None
    driver = None

    def setup_class(self):
        option = Options()
        option.debugger_address = "localhost:9222"
        driver = webdriver.Chrome(options=option)
        # driver.maximize_window()


        # 打开首页
        driver.get(self.main.url)
        self.driver = driver

    def teardown_class(self):
        self.driver.quit()

    def test_addDepartment(self):
        """
        1、打开首页
        2、跳转通讯录页面
        3、跳转添加部门页面
        4、添加部门
        5、断言：部门名称存在新添加部门
        """

        # 从首页跳转通讯录页面
        contactPage = self.main.goto_contactPage()

        # 从通讯录页面跳转添加部门页面
        addDeptPage = contactPage.goto_addDepartment()

        # 完成添加部门操作
        deptName = "质控中心"
        addDeptPage.addDepartment(deptName)

        time.sleep(2)

        findDeptName = contactPage.find_deptByName(deptName)
        assert deptName == findDeptName

