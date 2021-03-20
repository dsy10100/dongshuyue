#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

"""
使用cookie 登录企业微信，完成导入联系人，加上断言验证
"""


class TestCookie():
    def setup(self):
        option = Options()
        option.debugger_address = "localhost:9222"

        # 实例化driver
        self.driver = webdriver.Chrome()
        # 窗口最大化
        self.driver.maximize_window()
        # 设置隐式等待，避免网速慢等原因导致元素未被加载
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 关闭新开的浏览器，回收driver
        self.driver.quit()

    def test_cookie(self):
        cookies = self.driver.get_cookies()
        print(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # cookies=

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.CSS_SELECTOR, value=".index_service_cnt_itemWrap:nth-child(2)").click()
        # 上传文件使用元素.send_keys
        self.driver.find_element(By.ID, value="js_upload_file_input").send_keys(
            "/Users/apple/Desktop/data_selenium.xlsx")
        # 通过元素.text 去验证上传后的文件名称是否一致
        result = self.driver.find_element(By.ID, value="upload_file_name").text
        assert "data_selenium.xlsx" == result
