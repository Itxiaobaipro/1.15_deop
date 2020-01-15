from page.browse_all_goods_page import Browse_all_goods_Page
import unittest
from common.base import open_browser
from common.base import Base


class Test_browse_all_goods(unittest.TestCase):
    """浏览所有商品"""

    def setUp(self):
        """打开浏览器"""
        driver = open_browser("chrome")
        driver.maximize_window()
        self.browse = Browse_all_goods_Page(driver)
        url = "http:\\172.16.10.96:8080/ecshop"
        self.browse.open_url(url)

    def tearDown(self):
        """关闭浏览器"""
        self.browse.close()

    def test_browse_all_goods(self):
        self.browse.click_search()  # 点击首页搜索按钮
        self.browse.click_all_goods()  # 点击所有商品
        result = self.browse.is_next_page()  # 点击下一页
        self.assertTrue(result)  # 断言
