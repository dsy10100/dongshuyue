


class MemberInfoMorePage(BasePage):
    # 方法：个人信息更多操作页面跳转个人信息编辑页面
    def goto_memberInfoEditPage(self):
        self.findById("com.tencent.wework:id/b53").click()
        return MemberInfoEditPage(self.driver)