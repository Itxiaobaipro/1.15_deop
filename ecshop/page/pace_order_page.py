from common.base import Base
from common.base import open_browser


class Pace_Oder_Page(Base):
    """表现层  定位器"""
    # 登录
    username_loc = ("name", "username")  # 账号输入框
    password_loc = ("name", "password")  # 密码输入框
    submit_loc = ("name", "submit")  # 立即登录按钮
    search_loc = ("css selector", "input[name='imageField']")  # 搜索按钮
    choose_goods_camera_loc = ("css selector", "img[alt='智能相机']")  # 选择商品智能相机
    click_to_buy_loc = ("css selector", "td[class='td1']>a>img")  # 点击购买按钮
    settlement_loc = ("css selector", "img[alt='checkout']")  # 去结算按钮
    order_goods_name_loc = ("css selector", "div[class='flowBox']>table>tbody>tr:nth-child(2)>td:nth-child(1)>a")   # 打开订单后 商品名称
    order_goods_price_loc = ("css selector", "div[class='flowBox']>table>tbody>tr:nth-child(2)>td:nth-child(1)>a")  # 打开订单后 商品本店价
    order_goods_num_loc = ("css selector", "div[class='flowBox']>table>tbody>tr:nth-child(2)>td:nth-child(5)")   # 打开订单后 商品数量
    order_goods_all_price_loc = ("css selector", "div[class='flowBox']>table>tbody>tr:nth-child(2)>td:nth-child(6)")  # 打开订单后 商品小计
    our_price_loc = ("css selector", "div[class='flowBox']>table>tbody>tr:nth-child(2)>td:nth-child(1)>a")  # 提交订单页面-本店价显示信息
    sto_loc = ("css selector", "input[type='radio'][value='5']")  # 申通快递单选框
    post_office_loc = ("css selector", "input[type='radio'][value='6']")  # 邮局平邮单选框
    payment_balance_loc = ("css selector", "input[type='radio'][value='1']")  # 支付方式_余额支付单选框
    payment_bank_loc = ("css selector", "input[type='radio'][value='2']")  # 支付方式_银行汇款/转账单选框
    payment_cash_on_delivery_loc = ("css selector", "input[type='radio'][value='3']")  # 支付方式_货到付款单选框
    packing_no_loc = ("css selector", "input[name='pack'][value='0']")  # 商品包装_不要包装单选框
    packing_loc = ("css selector", "input[name='pack'][value='1']")  # 商品包装_精品包装单选框
    card_no_loc = ("css selector", "input[name='card'][value='0']")  # 祝福贺卡_不要贺卡单选框
    card_loc = ("css selector", "input[name='card'][value='1']")  # 祝福贺卡单选框
    card_greetings_loc = ("name", "card_message")  # 祝福贺卡_祝福语
    need_inv_loc = ("id", "ECS_NEEDINV")  # 其它信息-开发票复选框
    inv_type_loc = ("css selector", "select[name='inv_type']")  # 其它信息-发票类型下拉框
    inv_type_first_loc = ("css selector", "select[name='inv_type']>option:nth-child(1)")  # 其它信息-发票类型下拉框-1(1%)
    inv_type_second_loc = ("css selector", "select[name='inv_type']>option:nth-child(1)")  # 其它信息-发票类型下拉框-2(1.5%)
    inv_payee_loc = ("id", "ECS_INVPAYEE")  # 其它信息-开发票-发票抬头输入框
    postscript_loc = ("id", "postscript")  # 其它信息-订单附言输入框
    wait_all_goods_loc = ("css selector", "input[name='how_oos'][value='0']")  # 缺货处理-等待所有商品备齐后再发 单选框
    cancel_order_loc = ("css selector", "input[name='how_oos'][value='1']")  # 缺货处理-取消订单 单选框
    negotiate_loc = ("css selector", "input[name='how_oos'][value='2']")  # 缺货处理-与店主协商 单选框
    total_price_loc = ("css selector", "div[id='ECS_ORDERTOTAL']>table>tbody>tr:nth-of-type(2)>td>font:nth-of-type(1)")  # 商品总价信息显示
    accounts_payable_loc = ("css selector", "div[id='ECS_ORDERTOTAL']>table>tbody>tr:nth-of-type(3)>td>font")  # 应付款金额信息显示
    submit_order_loc = ("css selector", "input[type='image']")  # 提交订单按钮
    see_packing_loc = ("css selector", "a[href*='data/pack']")  # 点击查看商品包装
    see_card_loc = ("css selector", "a[href*='data/card']")  # 点击查看祝福贺卡
    after_order_balance_not_enough_loc = ("css selector", "p[style='font-size: 14px; font-weight:bold; color: red;']")  # 订单余额不足时 提交订单
    after_order_num_loc = ("css selector", "h6>font[style='color:red']")  # 订单提交后 订单号 显示信息
    after_order_distribution_loc = ("css selector", "table[width='99%']>tbody>tr>td>strong:nth-child(1)")  # 订单提交后 配送方式 显示信息
    after_order_payment_loc = ("css selector", "table[width='99%']>tbody>tr>td>strong:nth-child(2)")  # 订单提交后 付款方式 显示信息
    after_order_payable_loc = ("css selector", "table[width='99%']>tbody>tr>td>strong:nth-child(3)")  # 订单提交后 应付款金额 显示信息
    amend_goods_list_loc = ("css selector", "a[class='f6']")  # 修改商品列表 连接
    amend_address_loc = ("css selector", "a[href*='flow.php?']")  # 修改收货地址 连接
    logout_loc = ("css selector", "a[href*='user.php?']")  # 购物车页面 账户 退出 链接
    login_loc = ("css selector", "a[href*='user.php']")  # 登录 链接
    order_success_loc = ("css selector", "h6[style]")  # 订单提交成功文本

    # 操作层

    def search(self):
        """点击搜索按钮"""
        self.click(self.search_loc)

    def choose_goods_camera(self):
        """选择商品智能相机"""
        self.click(self.choose_goods_camera_loc)

    def click_to_buy(self):
        """点击购买按钮"""
        self.click(self.click_to_buy_loc)

    def settlement(self):
        """点击去支付按钮"""
        self.click(self.settlement_loc)

    def sto(self):
        """选择配送方式-申通快递单选框"""
        self.click(self.sto_loc)

    def post_office(self):
        """选择配送方式-邮局平邮单选框"""
        self.click(self.post_office_loc)

    def payment_balance(self):
        """选择支付方式-余额支付单选框"""
        self.click(self.payment_balance_loc)

    def payment_bank(self):
        """选择支付方式-银行汇款/转账单选框"""
        self.click(self.payment_bank_loc)

    def payment_cash_on_delivery(self):
        """选择支付方式-货到付款 单选框"""
        self.click(self.payment_cash_on_delivery_loc)

    def packing_no(self):
        """选择商品包装-不用包装 单选框"""
        self.click(self.packing_no_loc)

    def packing(self):
        """选择商品包装-精品包装单选框"""
        self.click(self.packing_loc)

    def click_packing(self):
        """点击查看包装"""
        self.click(self.see_packing_loc)
        self.quit_window()

    def card_no(self):
        """选择祝福贺卡-不要贺卡单选框"""
        self.click(self.card_no_loc)

    def card(self):
        """选择祝福贺卡-祝福贺卡单选框"""
        self.click(self.card_loc)

    def input_card_greetings(self, greetings):
        """输入祝福语"""
        self.send_keys(self.card_greetings_loc, greetings)

    def click_card(self):
        """点击查看祝福卡片"""
        self.click(self.see_card_loc)
        self.quit_window()

    def amend_goods_list(self):
        """点击修改商品列表"""
        self.click(self.amend_goods_list_loc)
        self.return_window()

    def amend_goods_address(self):
        """点击修改收货地址"""
        self.click(self.amend_address_loc)
        self.return_window()

    def need_inv(self):
        """选择开发票复选框"""
        self.click(self.need_inv_loc)

    def inv_type_first(self):
        """选择发票类型 1(1%)下拉框"""
        self.click(self.inv_type_first_loc)

    def inv_type_second(self):
        """选择发票类型 2(1.5%)下拉框"""
        self.click(self.inv_type_second_loc)

    def input_inv_payee(self, text):
        """输入发票抬头"""
        self.send_keys(self.inv_payee_loc, text)

    def input_postscript(self, text):
        """输入订单附言"""
        self.send_keys(self.postscript_loc, text)

    def wait_all_goods(self):
        """选择缺货处理-等待所有商品备齐后再发 单选框"""
        self.click(self.wait_all_goods_loc)

    def cancel_order(self):
        """选择缺货处理-取消订单 单选框"""
        self.click(self.cancel_order_loc)

    def negotiate(self):
        """选择缺货处理-与店主协商 单选框"""
        self.click(self.negotiate_loc)

    def submit_order(self):
        """点击提交订单"""
        self.click(self.submit_order_loc)

    # 登录流程
    def input_username(self, username):
        """输入账号"""
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        """输入密码"""
        self.send_keys(self.password_loc, password)

    def click_btn(self):
        """点击立即登录"""
        self.click(self.submit_loc)

    # 登录连接
    def click_login(self):
        """页面点击登录链接"""
        self.click(self.login_loc)

    # 退出登录
    def click_logout(self):
        """点击退出登录"""
        self.click(self.logout_loc)

    def get_success_text(self):
        """获取提交订单成功过后的文本"""
        return self.get_element_text(self.order_success_loc)

    def get_balance_text(self):
        """获取余额支付 余额不足时提交订单后的文本"""
        return self.get_element_text(self.after_order_balance_not_enough_loc)

    def is_text_in_text_success(self, text):
        """判断订单提交成功-文本是否在提交订单后的文本中"""
        return self.is_text_in_element(self.order_success_loc, text)

    # 判断订单提交成功-文本是否在提交订单后的文本中
    def is_text_in_text_balance(self, text):
        return self.is_text_in_element(self.after_order_balance_not_enough_loc, text)


if __name__ == '__main__':
    import time

    driver = open_browser()
    pec = Pace_Oder_Page(driver)
    pec.open_url("http://localhost:8080/ecshop/user.php")
    pec.input_username("admin123")
    pec.input_password("123456")
    pec.click_btn()
    pec.search()
    pec.choose_goods_camera()
    time.sleep(2)
    pec.click_to_buy()
    pec.settlement()
    time.sleep(2)
    pec.sto()
    pec.payment_bank()
    pec.packing()
    pec.card()
    pec.input_card_greetings("happy birthday")
    pec.need_inv()
    pec.inv_type_second()
    pec.input_inv_payee("迅捷科技")
    pec.input_postscript("三十秒后抵达")
    pec.wait_all_goods()
    pec.submit_order()
