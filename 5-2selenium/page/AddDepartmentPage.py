# -*- coding: utf-8 -*-
"""
@author：dongdong
写不明白了 回头补充
"""


class AddDepartmentPage(BasePage):
    def addDepartment(self, deptName):
        self.findByClass("input.qui_inputText.ww_inputText[name='name']").send_keys(deptName)
        self.findByClass(".qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list").click()
        self.findByClass(".js_party_list_container .jstree-anchor").click()
        self.findByClass(".ww_btn[d_ck='submit']").click()
