"""
封装的是表现层和操作层
登录界面
"""

from common.base import Base


class LoginPage(Base):
    # 封装表现层:制作定位器
    p_login_loc = ("css selector", "a[href='user.php']")  # 请登录按钮
    username_loc = ("name", "username")     # 用户名输入框
    password_loc = ("name", "password")     # 密码输入框
    remember_loc = ("id", "remember")       # 记住密码勾选框
    dsubmit_loc = ("name", "submit")         # 立即登录按钮/注册按钮
    element_text_loc = ("class name", "f4_b")  # 登录成功后的用户名
    problem_loc = ("link text", "密码问题")     # 密码问题
    email_loc = ("link text", "邮件")           # 邮件验证
    message_loc = ("link text", "短信验证")     # 短信验证链接


    # 封装操作层: 对表现层中的所有操作
    def click_p_login(self):
        """请登录按钮"""
        self.click(self.p_login_loc)

    def input_username(self, username):
        """输入用户名"""
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        """输入密码"""
        self.send_keys(self.password_loc, password)

    def click_remember_password(self):
        """点击记住密码勾选框"""
        self.click(self.remember_loc)

    def click_submit(self):
        """点击立即登录按钮"""
        self.click(self.dsubmit_loc)

    def click_problem(self):
        """点击密码问题链接"""
        self.click(self.problem_loc)

    def click_email_l(self):
        """点击邮件验证链接"""
        self.click(self.email_loc)

    def click_message(self):
        """点击短信验证链接"""
        self.click(self.message_loc)

    def input_email(self, email):
        """输入邮件"""
        self.send_keys(self.email_loc, email)

    def click_checkbox(self):
        """勾选框"""
        if self.is_selected(self.remember_loc):    # 判断勾选框是否被勾选,被勾选不执行
            pass
        else:
            self.click(self.remember_loc)

    def get_login_username(self, text):
        """获取登录后的用户名"""
        return self.is_text_in_element(self.element_text_loc, text)

    def is_login_successed(self, username):
        """判断登录是否成功"""
        return self.is_text_in_element(self.element_text_loc, username)





if __name__ == '__main__':
    from common.base import open_browser
    import time

    driver = open_browser("chrome")
    login = LoginPage(driver)
    # url = "http://localhost:8080/ecshop/index.php"
    url = "http: //localhost:8080/ecshop/user.php"# 登录页面地址
    login.open_url(url)
    # 输入用户名
    username = "admin"
    login.input_username(username)
    # 输入密码
    password = "123456"
    login.input_password(password)
    # 点击勾选框
    login.click_checkbox()
    # 点击登录
    login.click_submit()
    time.sleep(5)
    # 关闭
    login.close()
