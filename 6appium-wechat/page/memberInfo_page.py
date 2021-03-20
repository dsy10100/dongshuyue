


class MemberInfoPage(BasePage):
    # 跳转个人信息更多操作页面
    def goto_memberInfoMorePage(self):

        self.findById("com.tencent.wework:id/hjz").click()
        return MemberInfoMorePage(self.driver)