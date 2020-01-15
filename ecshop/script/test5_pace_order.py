from page.loginpage import LoginPage
from page.pace_order_page import Pace_Oder_Page
from common.base import open_browser
import unittest
import time


# from common.operation_data import OperationFile
# operation = OperationFile("login_data.csv")
# data1=operation.get_data_to_dict()
# data2 = operation.get_data_to_list()

# 2 创建测试类
# 提交订单类
class TestPaceOrder(unittest.TestCase):
    # 3 添加fixture
    def setUp(self):
        """打开浏览器进入网站"""
        driver = open_browser()
        driver.maximize_window()
        self.login = LoginPage(driver)
        self.login.open_url("http://localhost:8080/ecshop/index.php")
        """登录==>点击结算"""
        # 登录
        self.login.click_p_login()
        username = "admin123"
        self.login.input_username(username)
        # 输入密码
        password = "123456"
        self.login.input_password(password)
        # 点击勾选框
        self.login.click_checkbox()
        # 点击登录
        self.login.click_submit()

        # 点击搜索
        self.pace_order = Pace_Oder_Page(driver)
        self.pace_order.search()
        # 选择商品
        self.pace_order.choose_goods_camera()
        # 点击购买
        self.pace_order.click_to_buy()
        # 点击去结算
        self.pace_order.settlement()

    def tearDown(self):
        """关闭浏览器"""
        time.sleep(1)
        self.login.close()


    def test_pace_order_balance(self):
        """
        账户余额充足时,使用余额支付:
        提交订单:申通快递-余额付款-不要发票-不要包装-不要贺卡-不写附言-等待所有商品备齐后发货
        """
        # 选择申通快递
        self.pace_order.sto()
        # 选择余额支付
        self.pace_order.payment_balance()
        # 不选择发票

        # 选择不要包装
        self.pace_order.packing_no()
        # 选择不要贺卡
        self.pace_order.card_no()
        # 不写附言

        # 选择等待所有商品备齐后发货
        self.pace_order.wait_all_goods()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)

    def test_pace_order_no_balance(self):
        """
        账户余额不足时,使用余额支付:
        提交订单:申通快递-余额付款-不要发票-不要包装-不要贺卡-不写附言-等待所有商品备齐后发货
        :return:
        """
        # 点击退出登录
        self.pace_order.click_logout()
        # 点击登录
        self.pace_order.click_login()
        # 切换余额不足的账户重新登录
        # 登录
        self.login.input_username("admin")
        self.login.input_password("123456")
        self.login.click_submit()
        # 点击搜索
        self.pace_order.search()
        # 选择商品
        self.pace_order.choose_goods_camera()
        # 点击购买
        self.pace_order.click_to_buy()
        # 点击去结算
        self.pace_order.settlement()

        # 余额支付流程
        # 选择申通快递
        self.pace_order.sto()
        # 选择余额支付
        self.pace_order.payment_balance()
        # 不选择发票

        # 选择不要包装
        self.pace_order.packing_no()
        # 选择不要贺卡
        self.pace_order.card_no()
        # 不写附言

        # 选择等待所有商品备齐后发货
        self.pace_order.wait_all_goods()
        # 点击提交订单
        self.pace_order.submit_order()
        # 断言
        text = "您的余额不足以支付整个订单，请选择其他支付方式"
        result = self.pace_order.is_text_in_text_balance(text)
        self.assertTrue(result)

    def test_pace_order_payment_bank(self):
        """
        账户使用银行转账/汇款支付:
        提交订单:申通快递-银行转账/汇款-不要发票-不要包装-不要贺卡-不写附言-等待所有商品备齐后发货
        :return:
        """
        # 选择申通快递
        self.pace_order.sto()
        # 选择银行转账/汇款支付
        self.pace_order.payment_bank()
        # 不选择发票

        # 选择不要包装
        self.pace_order.packing_no()
        # 选择不要贺卡
        self.pace_order.card_no()
        # 不写附言

        # 选择等待所有商品备齐后发货
        self.pace_order.wait_all_goods()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)

    def test_pace_order_payment_cash_on_delivery(self):
        """
        账户使用货到付款:
        提交订单:申通快递-货到付款-不要包装-不要贺卡-不写附言-等待所有商品备齐后发货
        :return:
        """
        # 选择申通快递
        self.pace_order.sto()
        # 选择货到付款支付
        self.pace_order.payment_cash_on_delivery()
        # 不选择发票

        # 选择不要包装
        self.pace_order.packing_no()
        # 选择不要贺卡
        self.pace_order.card_no()
        # 不写附言

        # 选择等待所有商品备齐后发货
        self.pace_order.wait_all_goods()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)

    def test_pace_order_post_office(self):
        """
        账户选择 邮局平邮:
        提交订单:邮局平邮快递-银行转账/汇款-不要包装-不要贺卡-不写附言-等待所有商品备齐后发货
        :return:
        """
        # 选择邮局平邮
        self.pace_order.post_office()
        # 选择银行转账/汇款支付
        self.pace_order.payment_bank()
        # 不选择发票

        # 选择不要包装
        self.pace_order.packing_no()
        # 选择不要贺卡
        self.pace_order.card_no()
        # 不写附言

        # 选择等待所有商品备齐后发货
        self.pace_order.wait_all_goods()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)

    def test_pace_order_packing(self):
        """
        账户选择 精品包装
        提交订单:邮局平邮快递-银行转账/汇款-精品包装-不要贺卡-不写附言-等待所有商品备齐后发货
        :return:
        """
        # 选择邮局平邮
        self.pace_order.post_office()
        # 选择银行转账/汇款支付
        self.pace_order.payment_bank()
        # 不选择发票

        # 选择要包装
        self.pace_order.packing()
        # 选择不要贺卡
        self.pace_order.card_no()
        # 不写附言

        # 选择等待所有商品备齐后发货
        self.pace_order.wait_all_goods()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)

    def test_pace_order_card(self):
        """
        账户选择 精品包装 祝福贺卡 无祝福语
        提交订单:邮局平邮快递-银行转账/汇款-精品包装-祝福贺卡-不写附言-等待所有商品备齐后发货
        :return:
        """
        # 选择邮局平邮
        self.pace_order.post_office()
        # 选择银行转账/汇款支付
        self.pace_order.payment_bank()
        # 不选择发票

        # 选择要包装
        self.pace_order.packing()
        # 选择要贺卡
        self.pace_order.card()
        # 不写附言

        # 选择等待所有商品备齐后发货
        self.pace_order.wait_all_goods()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)

    def test_pace_order_card_greetings(self):
        """
        账户选择 要祝福贺卡 短句祝福语
        提交订单:邮局平邮快递-银行转账/汇款-精品包装-祝福贺卡-不写附言-等待所有商品备齐后发货
        :return:
        """
        # 选择邮局平邮
        self.pace_order.post_office()
        # 选择银行转账/汇款支付
        self.pace_order.payment_bank()
        # 不选择发票

        # 选择要包装
        self.pace_order.packing()
        # 选择要贺卡
        self.pace_order.card()
        # 不写附言
        self.pace_order.input_card_greetings("开开心心")
        # 选择等待所有商品备齐后发货
        self.pace_order.wait_all_goods()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)

    def test_pace_order_card_greetings_more(self):
        """
        账户选择 精品包装   长祝福语
        提交订单:邮局平邮快递-银行转账/汇款-精品包装-祝福贺卡-不写附言-等待所有商品备齐后发货
        :return:
        """
        # 选择邮局平邮
        self.pace_order.post_office()
        # 选择银行转账/汇款支付
        self.pace_order.payment_bank()
        # 不选择发票

        # 选择要包装
        self.pace_order.packing()
        # 选择要贺卡
        self.pace_order.card()
        # 不写附言
        self.pace_order.input_card_greetings(
            "若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若二人若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若而非二若若若若若若若若若热若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若二人若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若二乎乎或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或黑板报不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不么么么么么么么木木木木木木木木木木木木木木木木木木木木木木木木木木二人柔柔弱弱若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不柔柔弱弱若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若若呀呀呀呀呀呀晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕晕哒哒哒哒哒哒多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多")
        # 选择等待所有商品备齐后发货
        self.pace_order.wait_all_goods()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)

    def test_pace_order_inv_first_payee_no(self):
        """
        账户选择 要发票 发票类型1(1%) 无发票抬头
        提交订单:邮局平邮快递-银行转账/汇款-精品包装-祝福贺卡-不写附言-等待所有商品备齐后发货
        :return:
        """
        # 选择邮局平邮
        self.pace_order.post_office()
        # 选择银行转账/汇款支付
        self.pace_order.payment_bank()
        # 选择要发票
        self.pace_order.need_inv()
        # 选择发票类型1 1%
        self.pace_order.inv_type_first()
        # 不输入发票抬头
        # 选择要包装
        self.pace_order.packing()
        # 选择要贺卡
        self.pace_order.card()
        # 不写附言
        self.pace_order.input_card_greetings("开开心心")
        # 选择等待所有商品备齐后发货
        self.pace_order.wait_all_goods()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)

    def test_pace_order_inv_second_payee_no(self):
        """
        账户选择 要发票 发票类型2(2%) 无发票抬头
        提交订单:邮局平邮快递-银行转账/汇款-精品包装-祝福贺卡-不写附言-等待所有商品备齐后发货
        :return:
        """
        # 选择邮局平邮
        self.pace_order.post_office()
        # 选择银行转账/汇款支付
        self.pace_order.payment_bank()
        # 选择要发票
        self.pace_order.need_inv()
        # 选择发票类型2 2%
        self.pace_order.inv_type_second()
        # 不输入发票抬头
        # 选择要包装
        self.pace_order.packing()
        # 选择要贺卡
        self.pace_order.card()
        # 不写附言
        self.pace_order.input_card_greetings("开开心心")
        # 选择等待所有商品备齐后发货
        self.pace_order.wait_all_goods()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)

    def test_pace_order_inv_first_payee(self):
        """
        账户选择 要发票 发票类型1% 输入发票抬头
        提交订单:邮局平邮快递-银行转账/汇款-精品包装-祝福贺卡-写祝福语-不写附言-等待所有商品备齐后发货
        :return:
        """
        # 选择邮局平邮
        self.pace_order.post_office()
        # 选择银行转账/汇款支付
        self.pace_order.payment_bank()
        # 选择要发票
        self.pace_order.need_inv()
        # 选择发票类型1 1%
        self.pace_order.inv_type_first()
        # 输入发票抬头
        self.pace_order.input_inv_payee("cooper科技有限公司")
        # 选择要包装
        self.pace_order.packing()
        # 选择要贺卡
        self.pace_order.card()
        # 不写附言
        self.pace_order.input_card_greetings("开开心心")
        # 选择等待所有商品备齐后发货
        self.pace_order.wait_all_goods()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)

    def test_pace_order_inv_second_payee(self):
        """
        账户选择 要发票 发票类型2(2%) 输入发票抬头
        提交订单:邮局平邮快递-银行转账/汇款-精品包装-祝福贺卡-写祝福语-要发票-写发票抬头-不写附言-等待所有商品备齐后发货
        :return:
        """
        # 选择邮局平邮
        self.pace_order.post_office()
        # 选择银行转账/汇款支付
        self.pace_order.payment_bank()
        # 选择要发票
        self.pace_order.need_inv()
        # 选择发票类型2 2%
        self.pace_order.inv_type_second()
        # 输入发票抬头
        self.pace_order.input_inv_payee("cooper科技有限公司")
        # 选择要包装
        self.pace_order.packing()
        # 选择要贺卡
        self.pace_order.card()
        # 写附言
        self.pace_order.input_card_greetings("开开心心")
        # 选择等待所有商品备齐后发货
        self.pace_order.wait_all_goods()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)

    def test_pace_order_input_postscript(self):
        """
        账户选择 输入订单附言
        提交订单:邮局平邮快递-银行转账/汇款-精品包装-祝福贺卡-写附言-等待所有商品备齐后发货
        :return:
        """
        # 选择邮局平邮
        self.pace_order.post_office()
        # 选择银行转账/汇款支付
        self.pace_order.payment_bank()
        # 选择要发票
        self.pace_order.need_inv()
        # 选择发票类型2 2%
        self.pace_order.inv_type_second()
        # 输入发票抬头
        self.pace_order.input_inv_payee("cooper科技有限公司")
        # 选择要包装
        self.pace_order.packing()
        # 选择要贺卡
        self.pace_order.card()
        # 写祝福语
        self.pace_order.input_card_greetings("开开心心")
        # 写订单附言
        self.pace_order.input_postscript("最好下午送到")
        # 选择等待所有商品备齐后发货
        self.pace_order.wait_all_goods()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)

    def test_pace_order_cancel_order(self):
        """
        账户选择 取消订单
        提交订单:邮局平邮快递-银行转账/汇款-精品包装-祝福贺卡-不写附言-取消订单
        :return:
        """
        # 选择邮局平邮
        self.pace_order.post_office()
        # 选择银行转账/汇款支付
        self.pace_order.payment_bank()
        # 选择要发票
        self.pace_order.need_inv()
        # 选择发票类型2 2%
        self.pace_order.inv_type_second()
        # 输入发票抬头
        self.pace_order.input_inv_payee("cooper科技有限公司")
        # 选择要包装
        self.pace_order.packing()
        # 选择要贺卡
        self.pace_order.card()
        # 写祝福语
        self.pace_order.input_card_greetings("开开心心")
        # 写订单附言
        self.pace_order.input_postscript("最好下午送到")
        # 选择取消订单
        self.pace_order.cancel_order()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)

    def test_pace_order_negotiate(self):
        """
        账户选择 与店主协商
        提交订单:邮局平邮快递-银行转账/汇款-精品包装-祝福贺卡-不写附言-与店主协商
        :return:
        """
        # 选择邮局平邮
        self.pace_order.post_office()
        # 选择银行转账/汇款支付
        self.pace_order.payment_bank()
        # 选择要发票
        self.pace_order.need_inv()
        # 选择发票类型2 2%
        self.pace_order.inv_type_second()
        # 输入发票抬头
        self.pace_order.input_inv_payee("cooper科技有限公司")
        # 选择要包装
        self.pace_order.packing()
        # 选择要贺卡
        self.pace_order.card()
        # 写祝福语
        self.pace_order.input_card_greetings("开开心心")
        # 写订单附言
        self.pace_order.input_postscript("最好下午送到")
        # 选择与店主协商
        self.pace_order.negotiate()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)

    def test_pace_order_see_card_packing(self):
        """
        账户选择 查看祝福卡片和查看包装
        提交订单:邮局平邮快递-银行转账/汇款-精品包装-祝福贺卡-写附言-与店主协商
        :return:
        """
        # 选择邮局平邮
        self.pace_order.post_office()
        # 选择银行转账/汇款支付
        self.pace_order.payment_bank()
        # 选择要发票
        self.pace_order.need_inv()
        # 选择发票类型2 2%
        self.pace_order.inv_type_second()
        # 输入发票抬头
        self.pace_order.input_inv_payee("cooper科技有限公司")
        # 选择要包装
        self.pace_order.packing()
        # 选择要贺卡
        self.pace_order.card()
        # 写祝福语
        self.pace_order.input_card_greetings("开开心心")
        # 点击查看包装
        self.pace_order.click_packing()

        # 点击查看贺卡
        self.pace_order.click_card()
        # 写订单附言
        self.pace_order.input_postscript("最好下午送到")
        # 选择与店主协商
        self.pace_order.negotiate()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)

    def test_pace_order_amend_goods_list(self):
        """
        修改商品列表
        提交订单:邮局平邮快递-银行转账/汇款-精品包装-祝福贺卡-写附言-与店主协商
        :return:
        """
        # 点击修改商品列表
        self.pace_order.amend_goods_list()
        # 选择邮局平邮
        self.pace_order.post_office()
        # 选择银行转账/汇款支付
        self.pace_order.payment_bank()
        # 选择要发票
        self.pace_order.need_inv()
        # 选择发票类型2 2%
        self.pace_order.inv_type_second()
        # 输入发票抬头
        self.pace_order.input_inv_payee("cooper科技有限公司")
        # 选择要包装
        self.pace_order.packing()
        # 选择要贺卡
        self.pace_order.card()
        # 写祝福语
        self.pace_order.input_card_greetings("开开心心")
        # 点击查看包装
        self.pace_order.click_packing()

        # 点击查看贺卡
        self.pace_order.click_card()
        # 写订单附言
        self.pace_order.input_postscript("我要修改商品列表")
        # 选择与店主协商
        self.pace_order.negotiate()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)

    def test_pace_order_amend_goods_address(self):
        """
        修改商品收货地址
        提交订单:邮局平邮快递-银行转账/汇款-精品包装-祝福贺卡-写附言-与店主协商
        :return:
        """
        # 点击修改收货地址
        self.pace_order.amend_goods_address()

        # 选择邮局平邮
        self.pace_order.post_office()
        # 选择银行转账/汇款支付
        self.pace_order.payment_bank()
        # 选择要发票
        self.pace_order.need_inv()
        # 选择发票类型2 2%
        self.pace_order.inv_type_second()
        # 输入发票抬头
        self.pace_order.input_inv_payee("cooper科技有限公司")
        # 选择要包装
        self.pace_order.packing()
        # 选择要贺卡
        self.pace_order.card()
        # 写祝福语
        self.pace_order.input_card_greetings("开开心心")
        # 点击查看包装
        self.pace_order.click_packing()

        # 点击查看贺卡
        self.pace_order.click_card()
        # 写订单附言
        self.pace_order.input_postscript("我要修改商品列表")
        # 选择与店主协商
        self.pace_order.negotiate()
        # 点击提交订单
        self.pace_order.submit_order()
        """断言"""
        text = "您的订单已提交成功"
        result = self.pace_order.is_text_in_text_success(text)
        self.assertTrue(result)