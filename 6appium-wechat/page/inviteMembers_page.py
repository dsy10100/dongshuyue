


class InviteMembersPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    # 方法：邀请成员页面跳转手动添加成员页面
    def goto_addMembersManuallyPage(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.findByXpath("//*[@text='手动输入添加']").click()
        return AddMembersManuallyPage(self.driver)


