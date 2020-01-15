from common.operation_data import OperationFile
from common.base import Base
from page.loginpage import LoginPage
import ddt
import unittest



class RegisterPage(Base):
    free_register_loc = ("partial link text", "注册")  # 免费注册按钮
    username_loc = ("name", "username")     # 用户名输入框
    password_loc = ("name", "password")     # 密码输入框
    remember_loc = ("id", "remember")       # 记住密码勾选框
    submit_loc = ("name", "Submit")         # 立即登录按钮/注册按钮
    email_loc = ("name", "email")           # email输入框
    cpassword_loc = ("name", "confirm_password")  # 确认密码输入框
    qq_loc = ("name", "extend_field2")      # QQ输入框
    ophone_loc = ("name", "extend_field3")  # 办公电话输入框
    hphone_loc = ("name", "extend_field4")  # 家庭电话输入框
    phone_loc = ("name", "extend_field5")   # 手机输入框
    p_question_loc = ( "select[name='sel_question']")  # 密码提示问题下拉框
    answer_loc = ("name", "passwd_answer")      # 密码问题答案
    element_text_loc = ("class name", "f4_b")   # 登录成功后的用户名
    checkbox_loc = ("name", "agreement")        # 用户协议勾选框
    agreement_loc = ("css selector", "color:blue")    # 用户协议
    go_login_loc = ("partial link text", "我已有")    # 我已用账号,我要登录链接
    forget_password_loc = ("partial link text", "您忘记")  # 忘记密码链接

    # 封装操作层: 对表现层中的所有操作
    def click_free_register(self):
        """请注册按钮"""
        self.click(self.free_register_loc)

    def input_username(self, username):
        """输入用户名"""
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        """输入密码"""
        self.send_keys(self.password_loc, password)

    def click_remember_password(self):
        """点击记住密码"""
        self.click(self.submit_loc)

    def click_submit(self):
        """点击立即注册"""
        self.click(self.submit_loc)

    def get_login_username(self, text):
        """获取登录后的用户名"""
        return self.is_text_in_element(self.element_text_loc, text)

    def is_login_username(self, username):
        """判断登录是否成功"""
        return self.is_text_in_element(self.element_text_loc, username)

    def input_cpassword(self, cpassword):
        """输入确认密码"""
        self.send_keys(self.cpassword_loc, cpassword)

    def input_qq(self, qq):
        """输入qq"""
        self.send_keys(self.qq_loc, qq)

    def input_ophone(self, ophone):
        """输入办公电话"""
        self.send_keys(self.ophone_loc, ophone)

    def input_hphone(self, hphone):
        """输入家庭电话"""
        self.send_keys(self.hphone_loc, hphone)

    def input_phone(self, phone):
        """输入办公电话"""
        self.send_keys(self.phone_loc, phone)

    def input_qpassword(self):
        """密码提示问题下拉框"""
        return self.select_by_index(self.p_question_loc)

    def input_answer(self, answer):
        """密码问题答案"""
        self.send_keys(self.answer_loc, answer)

    def click_checkbox(self):
        """勾选框"""
        if self.is_selected(self.checkbox_loc):
            pass
        else:
            self.click(self.checkbox_loc)

    def agreement(self):
        """点击用户协议"""
        self.click(self.agreement_loc)

    def click_go_login(self):
        """已有账号,跳转至登录界面"""
        self.click(self.go_login_loc)

    def click_forget_password(self):
        """忘记密码链接"""
        self.click(self.forget_password_loc)

    def input_email(self, email):
        """输入邮件"""
        self.send_keys(self.email_loc, email)

    def click_alert_sure(self):
        """点击确定弹窗"""
        self.get_alert_ok()



if __name__ == '__main__':
    from common.base import open_browser
    import time
    from common.Faker import Faker_data

    # fake = Faker_data
    driver = open_browser("chrome")
    register = RegisterPage(driver)
    url = "http://localhost:8080/ecshop/index.php"  # ecshop商城地址
    register.open_url(url)
    # time.sleep(2)
    # 点击免费注册
    qd = register.click_free_register()

    # # # 输入用户名
    # username = "admin3"
    # register.input_username(username)
    # time.sleep(2)
    # # 输入密码
    # password = "1234567"
    # register.input_password(password)
    #
    # # 输入邮件
    # register.input_email("1234@qq.com")
    # # 输入确认密码
    # time.sleep(1)
    # register.input_cpassword("1234567")
    # time.sleep(1)
    # # 输入qq
    # register.input_qq("979565")
    # # 输入办公电话
    # time.sleep(1)
    # register.input_ophone("13989597999")
    # # 输入家庭电话
    # register.input_hphone("13989597998")
    # # 输入手机
    # register.input_phone("13989597997")
    # time.sleep(1)
    # # 随机密码提示问题
    # register.input_qpassword()
    # # 输入答案
    # register.input_answer(Faker_data().faker_pro())
    # # 勾选框
    # register.click_checkbox()
    # time.sleep(1)
    # 点击登录
    register.click_submit()
    # 输入为空捕获弹窗
    # alert = driver.switch_to_alert()
    # alert.accept()
    # 关闭
    time.sleep(3)
    register.close()