from page.loginpage import LoginPage
from common.base import open_browser
import unittest
import time

from page.consignee_address_page import ConsigneeInformation


class TestConsigneeAdress(unittest.TestCase):
    """"""

    def setUp(self):
        """用例执行前先打开浏览器连接ecshop"""
        driver = open_browser()
        driver.maximize_window()
        self.csif = ConsigneeInformation(driver)
        self.login = LoginPage(driver)
        self.login.open_url("http://localhost:8080/ecshop/index.php")  # 打开地址
        self.login.click_p_login()   # 请登录按钮
        self.username = "admin123"  # 输入用户名
        self.login.input_username(self.username)
        self.password = "123456"  # 输入密码
        self.login.input_password(self.password)
        self.login.click_submit()  # 点击登录
        self.csif.consignee_user_center()  # 点击用户中心
        self.csif.click_welcome_address()  # 点击用户中心的收货地址

    def tearDown(self):
        """在用例执行后关闭浏览器"""
        self.login.close()

    def test_case_1_consignee_address(self):
        """测试用例收货地址全部信息填写"""
        self.csif.consignee_province()
        # 收货人信息下拉框市的选择
        self.csif.consignee_city()
        # 收货人信息下拉框区的选择
        self.csif.consignee_district()
        # 填写收件人所有框
        self.csif.consignee_username()  # 输入用户名
        self.csif.consignee_addr()  # 输入地址
        self.csif.consignee_email()  # 输入邮箱号
        self.csif.consignee_tel()  # 输入手机号
        self.csif.consignee_mobile()  # 输入电话
        self.csif.consignee_zipcode()  # 输入邮编
        self.csif.click_consignee_add__new_addr()  # 点击新增收货地址


    # 修改
    def test_case_2_modify_address(self):
        """修改收货地址框"""
        self.csif.consignee_addr()  # 重新输入地址
        self.csif.consignee_modify_shopping_addr()  # 点击确认修改按钮##

    # 只有一个地址是 删除
    def test_case_3_del_address(self):
        """删除收货地址"""
        self.csif.consignee_user_center()
        self.csif.click_welcome_address()
        self.csif.consignee_del_shopping_addr()  # 点击确认删除按钮
        time.sleep(3)
        self.csif.click_alert_yes()


    # 必填项
    def test_case_4_must_address(self):
        """填写必填项新增地址"""
        # 新增收货人地址下拉框省的选择
        self.csif.consignee_province()
        # 新增收货人信息下拉框市的选择
        self.csif.consignee_city()
        # 新增收货人信息下拉框区的选择
        self.csif.consignee_district()
        # 新增填写收件人所有框
        self.csif.consignee_username()  # 输入用户名
        self.csif.consignee_addr()  # 输入地址
        self.csif.consignee_email()  # 输入邮箱号
        self.csif.click_consignee_add__new_addr()  # 点击新增收货地址


    def test_case_5_add_address(self):
        """新增地址填写全部信息"""
        # 收货人信息下拉框省的选择
        self.csif.consignee_province()
        # 收货人信息下拉框市的选择
        self.csif.consignee_city()
        # 收货人信息下拉框区的选择
        self.csif.consignee_district()
        self.csif.consignee_username()  # 输入用户名
        self.csif.consignee_addr()  # 输入地址
        self.csif.consignee_email()  # 输入邮箱号
        self.csif.consignee_tel()  # 输入手机号
        self.csif.click_consignee_add__new_addr()  # 点击新增收货地址

    # 新增填写收件人所有框
    def test_case_6_new_address(self):
        """添加一个新的收货地址"""
        # 新增收货人地址下拉框省的选择
        self.csif.add_province()
        # 新增收货人信息下拉框市的选择
        self.csif.add_city()
        # 新增收货人信息下拉框区的选择
        self.csif.add_district()
        # 新增填写收件人所有框
        self.csif.add_name()  # 输入用户名
        self.csif.add_addr()  # 输入地址
        self.csif.add_mail()  # 输入邮箱号
        self.csif.add_mobile()  # 输入手机号
        self.csif.add_tel()  # 输入电话
        self.csif.add_zipcode()  # 输入邮编
        self.csif.add_submit()  # 点击新增收货地址


if __name__ == '__main__':
    unittest.main()
