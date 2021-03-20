


class MemberInfoEditPage(BasePage):
    # 确定删除人员后跳转通讯录页面
    def editMemberInfo(self):
        # 点击该人员删除成员按钮
        self.findById("com.tencent.wework:id/e_1").click()
        # 点击确定删除按钮
        self.findById("com.tencent.wework:id/bfe").click()

        return ContactPage(self.driver)