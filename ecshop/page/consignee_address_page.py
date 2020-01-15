from common.base import Base
from common.base import open_browser
import time
from common.Faker import Faker_data
"""收货地址"""


class ConsigneeInformation(Base):
    """封装表现层:制作定位器"""
    consignee_username_loc = ("css selector", "input[name='consignee']")  # 收货人姓名输入框
    consignee_addr_loc = ("css selector", "input[name='address']")  # 收货人地址输入框
    consignee_tel_loc = ("css selector", "input[name='tel']")  # 收货人电话输入框
    consignee_mobile_loc = ("css selector", "input[name='mobile']")  # 收货人手机输入框
    consignee_email_loc = ("css selector", "input[name='email']")  # 收货人电子邮件输入框
    consignee_zipcode_loc = ("css selector", "input[name='zipcode']")  # 收货人邮政编码输入框
    consignee_country_loc = ("css selector", "select[name='country']>option")  # 收货人地址下拉框中国
    china_loc = ("name", "country")  # 国家下拉框
    province_loc = ("name", "province")  # 省下拉框
    city_loc = ("name", "city")  # 市下拉框

    consignee_province_loc = ("select[id='selProvinces_0']")  # 收货人地址下拉框省份
    consignee_city_loc = ("#selCities_0")  # 收货人地址 下拉框市
    consignee_district_loc = ("#selDistricts_0")  # 收货人地址 下拉框区

    consignee_add__new_addr_loc = ("css selector", "input[value='新增收货地址']")  # 新增收货地址框
    consignee_modify__shopping_addr_loc = ("class name", "bnt_blue_1")  # 确认修改收货地址框
    consignee_del_shopping_addr_loc = ("css selector", "input[class='bnt_blue']")  # 删除收货框按钮
    consignee_user_center_loc = ("css selector", "a[href]")  # ecshop右上角的用户中心框
    consignee_welcome_address_loc = ("link text", "收货地址")  # 用户中心的收货地址
    # ------------------------------------------------------------------------------------------------------
    # add_country_loc = ("xpath", "//form[last()]/table/tbody/tr[1]/td[2]/select[1]")  # 配送区域下拉框中国
    add_province_loc = ("#selProvinces_1")  # 配送区域下拉框省
    add_city_loc = ("#selCities_1")  # 配送区域下拉框 市
    add_district_loc = ("#selDistricts_1")  # 配送区域下拉框
    add_name_loc = ("xpath", "//form[last()]/table/tbody/tr[2]/td[2]/input")  # 定位收货人输入框 区
    add_mail_loc = ("xpath", "//form[last()]/table/tbody/tr[2]/td[4]/input")  # 定位邮箱输入框
    add_addr_loc = ("xpath", "//form[last()]/table/tbody/tr[3]/td[2]/input")  # 定位详细地址输入框
    add_zipcode_loc = ("xpath", "//form[last()]/table/tbody/tr[3]/td[4]/input")  # 定位邮编输入框
    add_tel_loc = ("xpath", "//form[last()]/table/tbody/tr[4]/td[2]/input")  # 定位电话输入框
    add_mobile_loc = ("xpath", "//form[last()]/table/tbody/tr[4]/td[4]/input")  # 定位手机输入框
    add_submit_loc = ("xpath", "/html/body/div[6]/div[2]/div/div/div/form[2]/table/tbody/tr[5]/td[2]/input[1]")  # 新增收货地址按钮
    faker = Faker_data()
    """封装操作层:对所有元素操作"""

    def consignee_username(self):
        """输入收货人用户名"""
        self.send_keys(self.consignee_username_loc, self.faker.faker_user())

    def consignee_addr(self):
        """输入收货人地址"""
        self.send_keys(self.consignee_addr_loc, self.faker.faker_add())

    def consignee_tel(self):
        """输入收货人电话"""
        self.send_keys(self.consignee_tel_loc, self.faker.faker_tel())

    def consignee_mobile(self):
        """输入收货人手机"""
        self.send_keys(self.consignee_mobile_loc, self.faker.faker_tel())

    def consignee_email(self):
        """输入收货人电子邮箱"""
        self.send_keys(self.consignee_email_loc, self.faker.faker_email())

    def consignee_zipcode(self):
        """输入收货人邮编"""
        self.send_keys(self.consignee_zipcode_loc, self.faker.faker_post())

    def consignee_country(self):
        """点击下拉框   选择中国"""
        self.select_by_index(self.consignee_country_loc)

    def consignee_province(self):
        """选择省"""
        self.select_by_index(self.consignee_province_loc)

    def consignee_city(self):
        """选择市"""
        self.select_by_index(self.consignee_city_loc)

    def consignee_district(self):
        """选择区"""
        self.select_by_index(self.consignee_district_loc)

    def consignee_modify_shopping_addr(self):
        """点击确认修改收货地址框"""
        self.click(self.consignee_modify__shopping_addr_loc)

    def consignee_del_shopping_addr(self):
        """点击删除收框按钮"""
        self.click(self.consignee_del_shopping_addr_loc)

    def consignee_user_center(self):
        """ecshop右上角用户中心框"""
        self.click(self.consignee_user_center_loc)

    def click_welcome_address(self):
        """点击用户中心下的收货地址"""
        self.click(self.consignee_welcome_address_loc)

    def click_consignee_add__new_addr(self):
        """点击新增收货地址"""
        self.click(self.consignee_add__new_addr_loc)

    # ..........................................................
    def add_province(self):
        """新增地址----选省"""
        self.select_by_index(self.add_province_loc)

    def add_city(self):
        """新增地址-----选市"""
        self.select_by_index(self.add_city_loc)

    def add_district(self):
        """新增地址----选区"""
        self.select_by_index(self.add_district_loc)

    def add_name(self):
        """新增地址----输入姓名"""
        self.send_keys(self.add_name_loc, self.faker.faker_user())

    def add_mail(self):
        """新增邮箱"""
        self.send_keys(self.add_mail_loc, self.faker.faker_add())

    def add_zipcode(self):
        """新增邮编"""
        self.send_keys(self.add_zipcode_loc, self.faker.faker_post())

    def add_addr(self):
        """新增收货地址"""
        self.send_keys(self.add_addr_loc, self.faker.faker_add())

    def add_tel(self):
        """新增电话号码"""
        self.send_keys(self.add_tel_loc, self.faker.faker_tel())

    def add_mobile(self):
        """新增手机号码"""
        self.send_keys(self.add_mobile_loc, self.faker.faker_tel())

    def add_submit(self):
        """新增收货地址按钮"""
        self.click(self.add_submit_loc)

    def click_alert_yes(self):
        """点击确认"""
        self.get_alert_ok()

    def click_alert_not(self):
        """点击取消"""
        self.get_alert_cancel()


if __name__ == '__main__':
    from page.loginpage import LoginPage

    driver = open_browser()
    csif = ConsigneeInformation(driver)
    login = LoginPage(driver)
    login.open_url("http://localhost:8080/ecshop/user.php")  # 打开地址
    username = "admin667"  # 输入用户名
    login.input_username(username)
    password = "admin123"  # 输入密码
    login.input_password(password)
    login.click_submit()  # 点击登录
    csif.consignee_user_center()  # 点击用户中心
    csif.click_welcome_address()  # 点击用户中心的收货地址
    csif.consignee_province()
    time.sleep(3)
    # 收货人信息下拉框市的选择
    csif.consignee_city()
    time.sleep(3)
    # 收货人信息下拉框区的选择
    csif.consignee_district()
    time.sleep(3)
    # 填写收件人所有框
    csif.consignee_username()  # 输入用户名
    csif.consignee_addr()  # 输入地址
    csif.consignee_email()  # 输入邮箱号
    csif.consignee_tel()  # 输入手机号
    csif.consignee_mobile()  # 输入电话
    csif.consignee_zipcode()  # 输入邮编
    csif.click_consignee_add__new_addr()  # 点击新增收货地址
    time.sleep(5)
