# -*- coding: utf-8 -*-
"""
@author：dongdong

"""
from selenium.webdriver.common.by import By


class BasePage:
    driver = None
    # 浏览器地址
    url = ""

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    # 提取公共查找元素方法
    def findByClass(self, classSelector):
        ClassEle = self.driver.find_element(By.CSS_SELECTOR, classSelector)
        return ClassEle

    def findElementsByClass(self, classSelector):
        ClassEles = self.driver.find_elements(By.CSS_SELECTOR, classSelector)
        return ClassEles

    def findById(self, idSelector):
        IdEle = self.driver.find_element(By.ID, idSelector)
        return IdEle
