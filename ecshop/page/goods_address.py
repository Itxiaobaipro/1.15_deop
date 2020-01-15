from common.base import Base
from common.Faker import Faker_data


class Address(Base):
    # 定位器
    country_loc = ("id", "selCountries_0")  # 国家下拉框
    provinces_loc = ("id", "selProvinces_0")  # 省份下拉框
    city_loc = ("id", "selCities_0")        # 市级下拉框
    area_loc = ("id", "selDistricts_0")     # 区下拉框
    consignee_loc = ("id", "consignee_0")   # 收货人姓名
    addr_loc = ("id", "address_0")      # 详细地址
    email_loc = ("id", "email_0")       # 邮件地址
    tel_loc = ("id", "tel_0")           # 电话
    mobile_loc = ("id", "mobile_0")     # 手机
    postal_loc = ("id", "zipcode_0")    # 邮政编码
    faker = Faker_data()

    country1_loc = ("id", "selCountries_1")  # 国家下拉框
    provinces1_loc = ("id", "selProvinces_1")  # 省份下拉框
    city1_loc = ("id", "selCities_1")  # 市级下拉框
    area1_loc = ("id", "selDistricts_1")  # 区下拉框
    consignee1_loc = ("id", "consignee_1")  # 收货人姓名
    addr1_loc = ("id", "address_1")  # 详细地址
    email1_loc = ("id", "email_1")  # 邮件地址
    tel1_loc = ("id", "tel_1")  # 电话
    mobile1_loc = ("id", "mobile_1")  # 手机
    postal1_loc = ("id", "zipcode_1")  # 邮政编码

    consignee_username_loc = ("css selector", "input[name='consignee']")  # 收货人姓名输入框
    consignee_addr_loc = ("css selector", "input[name='address']")  # 收货人地址输入框
    consignee_tel_loc = ("css selector", "input[name='tel']")  # 收货人电话输入框
    consignee_mobile_loc = ("css selector", "input[name='mobile']")  # 收货人手机输入框
    consignee_email_loc = ("css selector", "input[name='email']")  # 收货人电子邮件输入框
    consignee_zipcode_loc = ("css selector", "input[name='zipcode']")  # 收货人邮政编码输入框
    consignee_country_loc = ("css selector", "select[name='country']>option")  # 收货人地址下拉框中国
    china_loc = ("name", "country")  # 国家下拉框
    province_loc = ("name", "province")  # 省下拉框


    consignee_province_loc = ("select[id='selProvinces_0']")    # 收货人地址下拉框省份
    consignee_city_loc = ("#selCities_0")   # 收货人地址 下拉框市
    consignee_district_loc = ("#selDistricts_0")    # 收货人地址 下拉框区

    consignee_add__new_addr_loc = ("css selector", "input[value='新增收货地址']")  # 新增收货地址框
    consignee_modify__shopping_addr_loc = ("class name", "bnt_blue_1")      # 确认修改收货地址框
    consignee_del_shopping_addr_loc = ("css selector", "input[class='bnt_blue']")   # 删除收货框按钮
    consignee_user_center_loc = ("css selector", "a[href]")     # ecshop右上角的用户中心框
    consignee_welcome_address_loc = ("link text", "收货地址")   # 用户中心的收货地址
    add_province_loc = ("#selProvinces_1")      # 配送区域下拉框省
    add_city_loc = ("#selCities_1")         # 配送区域下拉框 市
    add_district_loc = ("#selDistricts_1")      # 配送区域下拉框
    add_name_loc = ("xpath", "//form[last()]/table/tbody/tr[2]/td[2]/input")  # 定位收货人输入框 区
    add_mail_loc = ("xpath", "//form[last()]/table/tbody/tr[2]/td[4]/input")  # 定位邮箱输入框
    add_addr_loc = ("xpath", "//form[last()]/table/tbody/tr[3]/td[2]/input")  # 定位详细地址输入框
    add_zipcode_loc = ("xpath", "//form[last()]/table/tbody/tr[3]/td[4]/input")  # 定位邮编输入框
    add_tel_loc = ("xpath", "//form[last()]/table/tbody/tr[4]/td[2]/input")  # 定位电话输入框
    add_mobile_loc = ("xpath", "//form[last()]/table/tbody/tr[4]/td[4]/input")  # 定位手机输入框
    add_submit_loc = ("xpath", "/html/body/div[6]/div[2]/div/div/div/form[2]/table/tbody/tr[5]/td[2]/input[1]")  # 新增收货地址按钮
    fake = Faker_data()

    # 表现层
    def click_country(self):
        """国家下拉框"""
        return self.select_by_index(self.country_loc)

    def click_provinces(self):
        """省份下拉框"""
        return self.select_by_index(self.provinces_loc)

    def click_city(self):
        """城市下拉框"""
        return self.select_by_index(self.city_loc)

    def click_area(self):
        """地区下拉框"""
        return self.select_by_index(self.area_loc)

    def consignee_username(self):
        """输入收货人用户名"""
        self.send_keys(self.consignee_loc, self.fake.faker_user())

    def consignee_addr(self):
        """输入收货人地址"""
        self.send_keys(self.addr_loc, self.fake.faker_add())

    def consignee_tel(self):
        """输入收货人电话"""
        self.send_keys(self.tel_loc, self.fake.faker_tel())

    def consignee_mobile(self):
        """输入收货人手机"""
        self.send_keys(self.mobile_loc, self.fake.faker_tel())

    def consignee_email(self):
        """输入收货人电子邮箱"""
        self.send_keys(self.email_loc, self.fake.faker_email())

    def click_consignee_add__new_addr(self):
        """点击新增收货地址"""
        self.click(self.consignee_add__new_addr_loc)

    def consignee_zipcode(self):
        """输入收货人邮编"""
        self.send_keys(self.postal_loc, self.fake.faker_post())

    def consignee_modify_shopping_addr(self):
        """点击确认修改收货地址框"""
        self.click(self.consignee_modify__shopping_addr_loc)

    def consignee_del_shopping_addr(self):
        """点击删除收框按钮"""
        self.click(self.consignee_del_shopping_addr_loc)

    def click_alert_yes(self):
        """点击确认"""
        self.get_alert_ok()

    def consignee_user_center(self):
        """ecshop右上角用户中心框"""
        self.click(self.consignee_user_center_loc)

    def click_welcome_address(self):
        """点击用户中心下的收货地址"""
        self.click(self.consignee_welcome_address_loc)

# 第二
    def consignee_username1(self):
        """输入收货人用户名"""
        self.send_keys(self.consignee1_loc, self.fake.faker_user())

    def consignee_addr1(self):
        """输入收货人地址"""
        self.send_keys(self.addr1_loc, self.fake.faker_add())

    def consignee_tel1(self):
        """输入收货人电话"""
        self.send_keys(self.tel1_loc, self.fake.faker_tel())

    def consignee_mobile1(self):
        """输入收货人手机"""
        self.send_keys(self.mobile1_loc, self.fake.faker_tel())

    def consignee_email1(self):
        """输入收货人电子邮箱"""
        self.send_keys(self.email1_loc, self.fake.faker_email())

    def consignee_zipcode1(self):
        """输入收货人邮编"""
        self.send_keys(self.postal1_loc, self.fake.faker_post())
