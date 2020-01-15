from common.base import open_browser
from page.registerpage import RegisterPage
from common.operation_data import OperationFile
from common.Faker import Faker_data
import time
import unittest



class TestRegister(unittest.TestCase):
    def setUp(self):
        driver = open_browser("chrome")
        self.register = RegisterPage(driver)
        url = "http://localhost:8080/ecshop/user.php?act=register"  # 输入ecshop商城地址
        self.register.open_url(url)

    def test_register1(self):
        """输入正确的信息"""
        # 注册数据随机生成
        # 将生成的数据写入表中
        info_data = []
        us = Faker_data().faker_user()  # 随机用户名
        self.register.input_username(us)  # 输入用户名
        info_data.append(us)  # 保存
        em = Faker_data().faker_email()  # 随机邮件
        self.register.input_email(em)  # 输入邮件
        info_data.append(em)
        pd = Faker_data().faker_password()  # 随机密码
        self.register.input_password(pd)  # 输入密码
        info_data.append(pd)
        # pd2 = pd                           # 确密码等于密码
        self.register.input_cpassword(pd)  # 输入确认密码

        q = Faker_data().faker_qq()  # 随机QQ
        self.register.input_qq(q)  # 输入qq
        info_data.append(q)
        te = Faker_data().faker_tel()  # 随机办公电话
        self.register.input_ophone(te)  # 输入办公电话
        info_data.append(te)
        te1 = Faker_data().faker_tel()  # 随机家庭电话
        self.register.input_hphone(te1)  # 输入家庭电话
        info_data.append(te1)
        te2 = Faker_data().faker_tel()  # 随机手机
        self.register.input_phone(te2)  # 输入手机
        info_data.append(te2)
        self.register.input_qpassword()  # 随机密码提示问题
        qpassword = self.register.input_qpassword()  # 获取密码提示问题
        info_data.append(qpassword)  # 添加到列表保存

        pr = Faker_data().faker_pro()  # 随机问题答案
        self.register.input_answer(pr)  # 输入答案
        info_data.append(pr)
        self.register.click_submit()    # 点击注册
        # self.register.click_alert_sure()
        # """断言"""
        # result = self.register.is_login_username(us)  # 获取注册成功后的用户名
        # self.assertEqual(result, us)

        print(info_data)
        filename = "register.xls"
        write_file = OperationFile(filename)
        write_file.write_data_to_excel(info_data)

    def test_register2(self):
        """验证只输入必填项"""
        info_data = []
        us = Faker_data().faker_user()  # 随机用户名
        self.register.input_username(us)  # 输入用户名
        info_data.append(us)  # 保存

        em = Faker_data().faker_email()  # 随机邮件
        self.register.input_email(em)  # 输入邮件
        info_data.append(em)

        pd = Faker_data().faker_password()  # 随机密码
        self.register.input_password(pd)  # 输入密码
        info_data.append(pd)

        # pd2 = pd  # 确密码等于密码
        self.register.input_cpassword(pd)  # 输入确认密码

        self.register.input_qq("")  # 输入qq
        info_data.append("")

        self.register.input_ophone("")  # 输入办公电话
        info_data.append("")

        self.register.input_hphone("")  # 输入家庭电话
        info_data.append("")

        te2 = Faker_data().faker_tel()  # 随机手机
        self.register.input_phone(te2)  # 输入手机
        info_data.append(te2)

        self.register.input_qpassword()  # 随机密码提示问题
        qpassword = self.register.input_qpassword()  # 获取密码提示问题
        info_data.append(qpassword)  # 添加到列表保存

        self.register.input_answer("")  # 输入答案
        info_data.append("")

        self.register.click_submit()   # 点击注册
        # """断言"""
        # result = self.register.is_login_username(us)  # 获取登录后的用户名
        # self.assertEqual(result, us)

        # self.register.click_alert_sure()
        write_file = OperationFile
        filename = "register.xls"
        write_file(filename).write_data_to_excel(info_data)

    def test_register3(self):
        """验证不输入必填项"""
        info_data = []
        us=self.register.input_username("")  # 用户名为空
        info_data.append("")
        self.register.input_email("")  # 邮件为空
        info_data.append("")
        self.register.input_password("")  # 密码为空
        info_data.append("")
        self.register.input_cpassword("")  # 确认密码为空

        q = Faker_data().faker_qq()  # 随机QQ
        self.register.input_qq(q)  # 输入qq
        info_data.append(q)

        te = Faker_data().faker_tel()  # 随机办公电话
        self.register.input_ophone(te)  # 输入办公电话
        info_data.append(te)

        te1 = Faker_data().faker_tel()  # 随机家庭电话
        self.register.input_hphone(te1)  # 输入家庭电话
        info_data.append(te1)

        self.register.input_phone("")  # 电话为空
        info_data.append("")

        self.register.input_qpassword()  # 随机密码提示问题
        qpassword = self.register.input_qpassword()  # 获取密码提示问题
        info_data.append(qpassword)  # 添加到表格保存

        pr = Faker_data().faker_pro()  # 随机问题答案
        self.register.input_answer(pr)  # 输入答案
        info_data.append(pr)
        time.sleep(5)
        self.register.click_submit()    # 点击注册
        # """断言"""
        # result = self.register.is_login_username(us)  # 获取登录后的用户名
        # self.assertEqual(result, us)

        # time.sleep(10)
        # self.register.click_alert_sure()

        write_file = OperationFile
        filename = "register.xls"
        write_file(filename).write_data_to_excel(info_data)

    def test_register4(self):
        """验证不输入邮件"""
        info_data = []
        us = Faker_data().faker_user()  # 随机用户名
        self.register.input_username(us)  # 输入用户名
        info_data.append(us)  # 保存
        self.register.input_email("")  # 输入邮件
        info_data.append("")
        pd = Faker_data().faker_password()  # 随机密码
        self.register.input_password(pd)  # 输入密码
        info_data.append(pd)
        # pd2 = pd  # 确密码等于密码
        self.register.input_cpassword(pd)  # 输入确认密码

        q = Faker_data().faker_qq()  # 随机QQ
        self.register.input_qq(q)  # 输入qq
        info_data.append(q)
        te = Faker_data().faker_tel()  # 随机办公电话
        self.register.input_ophone(te)  # 输入办公电话
        info_data.append(te)
        te1 = Faker_data().faker_tel()  # 随机家庭电话
        self.register.input_hphone(te1)  # 输入家庭电话
        info_data.append(te1)
        te2 = Faker_data().faker_tel()  # 随机手机
        self.register.input_phone(te2)  # 输入手机
        info_data.append(te2)
        self.register.input_qpassword()  # 随机密码提示问题
        qpassword = self.register.input_qpassword()  # 获取密码提示问题
        info_data.append(qpassword)  # 添加到列表保存
        pr = Faker_data().faker_pro()  # 随机问题答案
        self.register.input_answer(pr)  # 输入答案
        info_data.append(pr)
        # 创建对象
        write_file = OperationFile
        filename = "register.xls"
        write_file(filename).write_data_to_excel(info_data)
        self.register.click_submit()     # 点击注册
        # """断言"""
        # result = self.register.is_login_username(us)  # 获取登录后的用户名
        # self.assertEqual(result, us)
        # self.register.click_alert_sure()
        write_file = OperationFile
        filename = "register.xls"
        write_file(filename).write_data_to_excel(info_data)


    # def tearDown(self):
    #     """点击登录"""

if __name__ == '__main__':
    unittest.main()
