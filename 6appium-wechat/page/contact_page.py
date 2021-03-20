


class ContactPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    # 方法：通讯录页面跳转邀请成员页面
    def goto_inviteMembersPage(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.findByXpath("//*[@text='添加成员']").click()
        return InviteMembersPage(self.driver)

    # 方法：通讯录页面跳转个人信息页面
    def goto_memberInfotmationPage(self, name):
        self.findByXpath(f"//*[@text='{name}']").click()
        return MemberInfoPage(self.driver)

    # 方法：通讯录页面搜索成员
    def searchNoMember(self, name):
        # 点击搜索框
        self.findById("com.tencent.wework:id/hk9").click()
        # 输入搜索关键字
        self.findById("com.tencent.wework:id/g75").send_keys(name)
        # 无该成员时返回搜索结果
        searchResult = self.findById("com.tencent.wework:id/c5m").text
        logging.info(searchResult)
        return searchResult
