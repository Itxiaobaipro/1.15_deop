'''
测试用户登录
'''

from page.loginpage import LoginPage
from common.base import open_browser
from common.operation_data import OperationFile
import unittest
import time
import ddt

login_data = OperationFile("register.xls").get_data_to_dict()
login_data1 = OperationFile("login_2.xls").get_data_to_dict()
login_data2 = OperationFile("login_3.xls").get_data_to_dict()

@ddt.ddt
class LoginTest(unittest.TestCase):

    def setUp(self):
        driver = open_browser("chrome")
        self.login = LoginPage(driver)
        url = "http://localhost:8080/ecshop/user.php"  # 输入ecshop商城登录地址
        self.login.open_url(url)

    def tearDown(self):
        """关闭浏览器"""
        self.login.close()

    @ddt.data(*login_data)
    def test_login1(self, data):
        """用户名正确，密码正确登录验证"""
        self.login.input_username(data['username'])  # 输入用户名
        self.login.input_password(str(data['password']))
        self.login.click_submit()  # 点击立即登录
        # """断言"""
        # result = self.login.get_login_username(data['username'])  # 获取登录后的用户名
        # self.assertEqual(result, data["username"])

    @ddt.data(*login_data1)
    def test_login2(self, data):
        """用户名为空，密码正确"""
        self.login.input_username(data["username"])     # 输入用户名
        self.login.input_password(str(data["password"]))     # 输入密码
        self.login.click_submit()   # 点击立即登录

        # """断言"""
        # result = self.login.get_login_username(data["username"])      # 获取登录后的用户名
        # self.assertEqual(result, data["username"])



    @ddt.data(*login_data2)
    def test_login3(self, data):
        """用户名、密码为空"""
        self.login.input_username(data['username'])         # 输入用户名
        self.login.input_password(str(data['password']))    # 输入密码
        self.login.click_submit()       # 点击立即登录
        # """断言"""
        # result = self.login.get_login_username(data['username'])      # 获取登录后的用户名
        # self.assertEqual(result, data['username'])

    @ddt.data(*login_data)
    def test_login_remember_password(self, data):  # 测试用例的名称
        """测试记住密码登录"""
        self.login.input_username(data['username'])  # 输入用户名
        self.login.input_password(str(data['password']))  # 输入密码
        self.login.click_remember_password()  # 点击输入确认密码勾选框
        self.login.click_submit()  # 点击立即登录
        # """断言"""
        # result = self.get_login_username()  # 获取登录后的用户名
        # self.assertEqual(result, data["username"])

    @ddt.data(*login_data)
    def test_login(self, data):
        """测试不记住密码登录"""
        # 输入用户名
        self.login.input_username(data['username'])  # 输入用户名
        # 输入密码 不能
        self.login.input_password(str(data['password']))  # 输入密码
        # 点击立即登录
        self.login.click_submit()
        # """断言"""
        # result = self.login.is_login_successed(username)  # 判断是否登录成功
        # self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
