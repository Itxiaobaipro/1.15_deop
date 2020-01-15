# from page.loginpage import LoginPage
import time

from common.base import open_browser
import unittest
import ddt
from page.shopping_car_page import Shopping


# 添加商品
# login_dir =OperationFlie("userdata.xlsx").get_data_to_dict()
class TestLog(unittest.TestCase):
    def setUp(self):
        # 打开浏览器
        from page.loginpage import LoginPage
        driver = open_browser("chrome")
        register1 = LoginPage(driver)
        driver.maximize_window()
        self.login = Shopping(driver)
        url = "http://localhost:8080/ecshop/index.php"  # ecshop商城地址
        self.login.open_url(url)
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
        time.sleep(2)



    def tearDown(self):
        """关闭浏览器"""
        self.login.close()

    def test_case_0_0(self):
        """添加商品"""
        self.login.click_portable_source()
        self.login .click_portable_battery()
        # 点击购买
        self.login.click_purchase()
        # 断言
        lst = self.login.goods_style_name_2_shop()
        self.assertTrue(lst)

    # 添加不同的商品
    def test_case_1_0(self):
        # 点击搜索框
        self.login.input_search_kuag("平衡车")
        # 点击界面的平衡车
        self.login.click_balancing()
        # 点击购买
        self.login.click_purchase()
        # 断言
        lst = self.login.goods_style_name_2_shop()
        self.assertTrue(lst)

    # 购买商品时输入数量点击购买
    def test_case_2_0(self):
        # 点击搜索框
        self.login.input_search_kuag("平衡车")
        # 点击界面平衡车
        self.login.click_balancing()
        # 清空
        self.login.clear_purchase_number()
        # 输入要购买的数量
        self.login.send_keys_input_box("1")
        # 点击购买
        self.login.click_purchase()
        # 返回
        self.login.back()
        # 点击购物车
        self.login.click_shop_cart()
        # 断言
        lst = self.login.goods_style_name_2_shop()
        self.assertTrue(lst)

    # 购买99个平衡车
    def test_case_3_0(self):
        # 点击搜索框
        self.login.input_search_kuag("平衡车")
        # 点击界面平衡车
        self.login.click_balancing()
        # 清空
        self.login.clear_purchase_number()
        # 输入要购买的数量
        self.login.send_keys_input_box("99")
        # 点击购买
        self.login.click_purchase()
        # 点击首页
        self.login.click_homepage_button()
        # 点击购物车
        self.login.click_shop_cart()
        # 断言
        lst = self.login.goods_style_name_2_shop()
        self.assertTrue(lst)

    # 购买49个平衡车
    def test_case_4_0(self):
        # 点击搜索框
        self.login.input_search_kuag("平衡车")
        # 点击界面平衡车
        self.login.click_portable_battery()
        # 清空
        self.login.clear_purchase_number()
        # 输入要购买的数量
        self.login.send_keys_input_box("49")
        # 点击购买
        self.login.click_purchase()
        # 返回
        self.login.back()
        # 点击购物车
        self.login.click_shop_cart()
        # 断言
        lst = self.login.goods_style_name_2_shop()
        self.assertTrue(lst)

    # 购买两次平衡车验证购物车是否增加
    def test_case_5_0(self):
        # 点击搜索框
        self.login.input_search_kuag("平衡车")
        # 点击界面平衡车
        self.login.click_balancing()
        # 清空
        self.login.clear_purchase_number()
        # 输入要购买的数量
        self.login.send_keys_input_box("1")
        # 点击购买
        self.login.click_purchase()
        # 返回
        self.login.back()
        # 返回
        self.login.back()
        # 点击界面平衡车
        self.login.click_balancing()
        # 清空
        self.login.clear_purchase_number()
        # 输入要购买的数量
        self.login.send_keys_input_box("3")
        # 点击购买
        self.login.click_purchase()
        # 返回
        self.login.back()
        # 点击购物车
        self.login.click_shop_cart()
        # 断言
        lst = self.login.goods_style_name_2_shop()
        self.assertTrue(lst)

    # 清空购物车
    def test_case_6_0(self):
        # 点击搜索框
        self.login.input_search_kuag("平衡车")
        # 点击界面的平衡车
        self.login.click_balancing()
        # 点击购买
        self.login.click_purchase()
        # 点击首页
        self.login.click_homepage_button()
        # 点击购物车
        self.login.click_shop_cart()
        # 清空购物车
        self.login.click_empty_cart()
        # 断言
        lst = self.login.goods_style_name_shop("平衡车")
        self.assertEqual(lst, self.login.goods_style_name_2_shop(), msg="删除成功")

    # 验证更新购物车
    def test_case_7_0(self):
        # 点击搜索框
        self.login.input_search_kuag("平衡车")
        # 点击界面的平衡车
        self.login.click_balancing()
        # 点击购买
        self.login.click_purchase()
        # 点击首页
        self.login.click_homepage_button()
        # 点击购物车
        self.login.click_shop_cart()
        # 更新购物车
        self.login.clear_input_id()
        self.login.input_id_loc("2")
        self.login.click_updata_cart()
        # 断言
        run = self.login.right_shop(self.login.right_loc)
        self.assertEqual(run, self.login.right_shop(self.login.right_loc))

    # 验证去结算按钮
    def test_case_8_0(self):
        # 点击搜索框
        self.login.input_search_kuag("平衡车")
        # 点击平衡车
        self.login.click_balancing()
        # 点击购买
        self.login.click_purchase()
        # 点击去结算
        self.login.click_settlement()

    # 验证继续购物按钮
    def test_case_9_0(self):
        # 点击搜索框
        self.login.input_search_kuag("平衡车")
        # 点击平衡车
        self.login.click_balancing()
        # 点击购买
        self.login.click_purchase()
        # 点击继续购物
        self.login.click_shop_cart()
        # 点击平衡车
        self.login.click_balancing()
        # 点击购买
        self.login.click_purchase()
        # #点击去结算
        # time.sleep(2)
        # self.login.click_settlement()
        # time.sleep(2)
        # 断言
        run = self.login.right_shop(self.login.right_loc)
        self.assertEqual(run, self.login.right_shop(self.login.right_loc))

    # 验证删除与收藏按钮点击确认
    def test_case_1_1(self):
        # 点击搜索框
        self.login.input_search_kuag("平衡车")
        # 点击平衡车
        self.login.click_balancing()
        # 点击购买
        self.login.click_purchase()
        # 点击删除和收藏按钮
        self.login.click_delete()
        # 捕获弹窗并点击确认
        self.login.click_alert()
        # 点击去结算
        self.login.click_settlement()

    # 验证删除与收藏按钮点击取消
    def test_case_1_2(self):
        # 点击搜索框
        self.login.input_search_kuag("平衡车")
        # 点击平衡车
        self.login.click_balancing()
        # 点击购买
        self.login.click_purchase()
        # 点击首页
        self.login.click_homepage_button()
        # 点击购物车
        self.login.click_shop_cart()
        # 点击删除与收藏按钮
        self.login.click_delete()
        # 捕获弹窗点击取消
        self.login.click_alert_dis()

# 验证购买两个商品是否能成功添加到购物车
    def test_case_1_3(self):
        # 点击搜索框
        self.login.input_search_kuag("平衡车")
        # 点击界面平衡车
        self.login.click_balancing()
        # 清空
        self.login.clear_purchase_number()
        # 输入要购买的数量
        self.login.send_keys_input_box("1")
        # 点击购买
        self.login.click_purchase()
        # 点击继续购物
        self.login.click_continue_shop()
        # 点击智能相机
        self.login.click_goodsimg()
        # 点击购买
        self.login.click_purchase()
        # 点击首页
        self.login.click_homepage_button()
        # 断言
        lst = self.login.goods_style_name_2_shop()
        self.assertTrue(lst, msg="添加成功")

    # 验证购买商品修改商品数量点击去结算界面跳转成功
    def test_case_1_4(self):
        # 点击搜索框
        self.login.input_search_kuag("智能相机")
        # 点击智能相机
        self.login.click_goodsimg()
        # 点击购买
        self.login.click_purchase()
        # 清空
        self.login.clear_input_id()
        # 输入数量
        self.login.input_id_loc("2")
        # 点击更新
        self.login.click_updata_cart()
        # 点击去结算
        self.login.click_settlement()


if __name__ == '__main__':
    unittest.main()
