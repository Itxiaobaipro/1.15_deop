from common.base import Base


class Shopping(Base):
    # 封装定位器
    goods_loc = ("css selector", "div.goodsItem>a")
    search_kuag_loc = ("id", "keyword")     # 搜索框
    search_button_loc = ("name", "imageField")    # 搜索按钮
    homepage_button_loc = ("class name", "cur")   # 首页按钮
    clothing_loc = ("link text", "服装")          # 服装按钮
    portable_source_loc = ("link text", "移动电源")         # 移动电源按钮
    digital_fashion_loc = ("link text", "数码时尚")         # 数码时尚按钮
    electric_appliance_loc = ("link text", "家用电器")      # 家用电器按钮
    intelligent_hardware_loc = ("link text", "智能硬件")    # 智能硬件按钮
    phone_type_loc = ("link text", "手机类型")      # 手机类型按钮
    phone_loc = ("link text", "手机")               # 手机按钮
    rechargeable_card_loc = ("link text", "充值卡")    # 充值卡按钮
    parts_loc = ("link text", "配件")               # 配件按钮
    purchase_loc = ("css selector", "img[src='themes/default/images/buybtn1.png']")         # 购买按钮
    shop_collection_loc = ("css selector", "img[src='themes/default/images/bnt_colles.gif']")    # 收藏按钮
    share_loc = ("css selector", "img[src='themes/default/images/bnt_recommend.gif']")      # 分享按钮
    purchase_number_loc = ("id", "goods_number_60")     # 购买数量输入框
    settlement_loc = ("css selector", "img[src='themes/default/images/checkout.gif']")      # 去结算按钮
    empty_cart_loc = ("css selector", "input[value='清空购物车']")   # 清空购物车
    update_cart_loc = ("css selector", "input[value='更新购物车']")  # 更新购物车
    continue_shop_loc = ("css selector", "img[alt='continue']")      # 继续购物
    shop_cart_loc = ("css selector", "[title='查看购物车']")         # 购物车按钮
    bnt_blue_loc = ("class name", "bnt_blue_2")    # 配送按钮
    delete_loc = ("link text", "删除")             # 购物车里面的删除
    car_collection_loc = ("link text", "放入收藏夹")   # 收藏按钮
    goods_style_name_loc = ("class name", "goods_style_name")  # 购买商品里面的商品名称
    goods_style_name_2_loc = ("class name", "f6")  # 购物车里面的商品名称
    goodsimg_loc = ("class name", "goodsimg")  # 智能照相机
    input_box_loc = ("name", "number")  # 输入框输入数量
    input_id = ("class name", "inputBg")  # 购物车里面的输入框
    right_loc = ("css selector", "td[alian=right]")  # 小计
    # 商品
    portable_battery_loc = ("class name", "img-box")    # 充电宝
    balancing_car_loc = ("css selector", "div.all_ms>a:nth-of-type(3)")  # 平衡车

    # 操作层
    def input_search_kuag(self, text):
        """点击搜索框"""
        self.send_keys(self.search_kuag_loc, text)

    def right_shop(self, text):
        """小计获取文本"""
        return self.is_text_in_element(self.right_loc, text)

    def click_alert(self):
        """捕获弹窗并点击确认"""
        self.get_alert_ok()

    def click_search_button(self):
        """点击搜索按钮"""
        self.click(self.search_button_loc)

    def click_homepage_button(self):
        """首页按钮"""
        self.click(self.homepage_button_loc)

    def click_clothing(self):
        """点击服装按钮"""
        self.click(self.clothing_loc)

    def click_portable_source(self):
        """点击移动电源"""
        self.click(self.portable_source_loc)

    def click_digital_fashion(self):
        """点击数码时尚"""
        self.click(self.digital_fashion_loc)

    def click_electric_appliance(self):
        """点击家用电器"""
        self.click(self.electric_appliance_loc)

    def click_intelligent_hardware(self):
        """点击智能硬件"""
        self.click(self.intelligent_hardware_loc)

    def click_phone_type(self):
        """点击手机类型"""
        self.click(self.phone_type_loc)

    def click_phone(self):
        """点击手机"""
        self.click(self.phone_loc)

    def click_rechargeable_card(self):
        """点击充值卡"""
        self.click(self.rechargeable_card_loc)

    def click_parts(self):
        """点击配件"""
        self.click(self.parts_loc)

    def click_portable_battery(self):
        """点击商品充电宝"""
        self.click(self.portable_battery_loc)

    def click_balancing(self):
        """点击商品平衡车"""
        self.click(self.balancing_car_loc)

    def click_purchase(self):
        """点击立即购买"""
        self.click(self.purchase_loc)

    def click_collection(self):
        """收藏按钮"""
        self.click(self.shop_collection_loc)

    def click_share(self):
        """分享按钮"""
        self.click(self.share_loc)

    def click_purchase_number(self):
        """购买数量按钮"""
        self.click(self.purchase_number_loc)

    def click_settlement(self):
        """点击去结算按钮"""
        self.click(self.settlement_loc)

    def click_empty_cart(self):
        """点击清空购物车"""
        self.click(self.empty_cart_loc)

    def click_updata_cart(self):
        """点击更新购物车"""
        self.click(self.update_cart_loc)

    def click_continue_shop(self):
        """点击继续购物"""
        self.click(self.continue_shop_loc)

    def click_shop_cart(self):
        """点击购物车"""
        self.click(self.shop_cart_loc)

    def click_bnt_blue(self):
        """点击配送按钮"""
        self.click(self.bnt_blue_loc)

    def clear_purchase_number(self):
        """清空购买数量"""
        self.clear(self.purchase_number_loc)

    def get_goods_title(self):
        """获取所有商品标题"""
        self.click_search_button()
        goods_elements = self.find_elements(self.goods_loc)
        goods_title = []
        for element in goods_elements:
            title = element.get_attribute("title")
            goods_title.append(title)
        return goods_title

    def click_all_goods(self):
        """点击所有商品"""
        goods_title = self.get_goods_title()
        for title in goods_title:
            goods_loc = ("css selector", f"a[title='{title}']")  # 重写定位器
            self.click(goods_loc)
            time.sleep(2)
            self.click(self.purchase_loc)
            time.sleep(10)
            self.back()
            self.back()

    def click_car_collection(self):
        """点击购物车中的收藏按钮"""
        self.click(self.car_collection_loc)

    def click_delete(self):
        """点击删除按钮"""
        self.click(self.delete_loc)

    def click_alert_sure(self):
        """点击确定弹窗"""
        self.get_alert_ok()

    def click_alert_dis(self):
        """捕获弹窗并点击取消"""
        self.get_alert_cancel()


    def click_goodsimg(self):
        """点击智能照相机"""
        self.click(self.goodsimg_loc)

    def goods_style_name_shop(self, text):
        """购买商品的名称"""
        return self.is_text_in_element(self.goods_style_name_loc,text)

    def goods_style_name_2_shop(self):
        """购物车的商品名称"""
        return self.get_element_text(self.goods_style_name_2_loc)

    def send_keys_input_box(self, text):
        """输入商品数量"""
        self.send_keys(self.input_box_loc, text)

    def input_id_loc(self, num):
        """购物车中输入数量"""
        self.send_keys(self.input_id, num)

    def clear_input_id(self):
        """清空购物车里面的输入框"""
        self.clear(self.input_id)

if __name__ == '__main__':
    from common.base import Base
    from common.base import open_browser
    import time
    from page.loginpage import LoginPage

    driver = open_browser("chrome")
    register1 = LoginPage(driver)
    register = Shopping(driver)
    url = "http://localhost:8080/ecshop/index.php"  # ecshop商城地址
    register.open_url(url)
    # 输入用户名
    register1.click_p_login()
    username = "admin"
    register1.input_username(username)
    # 输入密码
    password = "123456"
    register1.input_password(password)
    # 点击勾选框
    register1.click_checkbox()
    # 点击登录
    register1.click_submit()
    # # 点击购物车
    # register.click_shop_cart()

    # register.input_search_kuag("3g手机")
    # time.sleep(1)
    # register.click_search_button()
    # time.sleep(2)
    # register.click_homepage_button()
    # time.sleep(1)
    register.click_portable_source()  # 点击移动电源
    register.click_portable_battery()  # 点击充电宝
    register.click_purchase()  # 立即购买
    # register.click_settlement()  # 去结算
    # register.click_bnt_blue()
    register.click_car_collection()  # 点击收藏按钮
    # register.click_delete()   # 点击删除按钮
    register.click_alert_sure()    # 弹窗点击
    # time.sleep(1)
    # register.back()
    time.sleep(2)
    register.close()
