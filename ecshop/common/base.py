"""
对selenium的二次封装
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import random
import time


def open_browser(browser='Chrome'):
    """
    打开浏览器
    :param browser:  浏览器名称
    :return:
    """

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser.lower() == "ie":
        driver = webdriver.Ie()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    else:
        driver = None
        print("请输入正确的浏览器,例如:chrome,firefox,ie")
    return driver


class Base:
    # 封装是项目中常用的基本方法
    def __init__(self, driver):
        # 初始化
        self.driver = driver

    def open_url(self, url):
        """
        输入网址
        :param url: 网址
        :return:
        """
        self.driver.get(url)
        self.driver.maximize_window()  # 浏览器最大化

    def find_element(self, locator: tuple = None, timeout=10):
        """
        定位元素,定位单个元素,如果找到元素返回元素本身,没找到返回False
        :param locator: 定位器
        :param timeout: 最长等待时间
        :return: element
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except:
            print(f"元素{locator}没找到")
            return False

    def find_elements(self, locator, timeout=10):
        """
        定位一组元素
        :param locator:定位器
        :param timeout:最大等待时间
        :return: elements
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            return element
        except:
            print(f"元素{locator}没找到")
            return False

    def click(self, locator):
        """
        元素点击
        :param locator: 定位器
        :return:
        """
        element = self.find_element(locator)  # 找元素
        element.click()  # 点击元素

    def send_keys(self, locator, text):
        """
        元素输入
        :param locator: 定位器
        :param text: 输入内容
        :return:
        """
        element = self.find_element(locator)  # 找元素
        element.clear()  # 清空
        element.send_keys(text)  # 输入

    def is_text_in_element(self, locator, text, timeout=10):
        """
        判断给定的文本是在元素中,如果在返回Ture,如果不在返回False
        :param locator: 定位器
        :param text: 输入的内容
        :param timeout:  最长等待时长
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def close(self):
        """关闭浏览器"""
        self.driver.quit()

    def get_element_text(self, locator):
        """获取文本"""
        try:
            element = self.find_element(locator)
            return element.text
        except:
            return False

    def get_value(self, locator):
        """获取value值"""
        element_value = self.find_element(locator)
        element_value.get_attribute("value")

    def is_selected(self, locator):
        """判断勾选框是否被勾选"""
        element = self.find_element(locator)
        return element.is_selected()

    def is_checkbox(self, locator):
        """复选框"""
        checkboes = self.find_elements(locator)
        for checkbox in checkboes:  # 遍历所有复选框元素
            if checkbox.is_selected():  # 判断复选框是否被选中,如果选中不点击,反之点击;选中所有的复选框
                pass
            else:
                checkbox.click()

    def select_partial_checkboxes(self, locator, choose):
        """复选框操作"""
        elements = self.find_elements(locator)
        for element in elements:  # 遍历所有复选框元素
            if element.get_attribute("name") in choose:  # 判断元素的value属性值是否属于要选择的选项
                if element.is_selected():  # 判断复选框是否被选中,如果选中不点击,反之点击;选中所有的复选框
                    pass
                else:
                    element.click()
            else:
                if element.is_selected():
                    element.click()
                else:
                    pass

    def select_checkbox(self, locator):
        """选择单选框操作"""
        element = self.find_element(locator)
        if element.is_selected():  # 判断复选框是否被选中,如果选中不点击,反之点击;选中所有的复选框
            pass
        else:
            element.click()

    def select_by_index(self, expression):
        """
        操作下拉框菜单,通过索引;随机选择下拉菜单中菜单
        :param expression: 元素定位css表达式
        :param i: 索引    默认为 1
        :return:
        """
        loc = ("css selector", expression)  # 下拉菜单标签
        loc_1 = ("css selector", f"{expression}>option")
        element = self.find_element(loc)  # 定位下拉菜单的标签
        elements = self.find_elements(loc_1)  # 定位所有选项标签
        count_option = len(elements)  # 得到选项数量
        num = random.randint(1, count_option - 1)  # 随机数
        Select(element).select_by_index(num)
        return elements[num].text

    def back(self):
        """
        浏览器后退
        :return:
        """
        self.driver.back()

    def get_alert_ok(self):
        """获取弹窗,点击确认"""
        alert = self.driver.switch_to.alert()
        time.sleep(1)
        alert.accept()

    def get_alert_cancel(self):
        """获取弹窗,点击取消"""
        alert = self.driver.switch_to.alert()
        alert.dismiss()

    def clear(self, locator):
        """清空"""
        self.find_element(locator).clear()
        # self.driver.clear(locator)
    def quit_window(self):
        """多窗口操作-退出新窗口"""
        handle = self.driver.current_window_handle
        self.driver.switch_to_window(handle)

    def return_window(self):
        """返回同一窗口上一个页面"""
        self.driver.back()




if __name__ == '__main__':
    from page.shopping_car_page import Shopping
    import time

    driver = open_browser()
    base = Base(driver)
    url = "http://localhost:8080/ecshop/user.php"
    base.open_url(url)  # 打开网址
    # search_loc = ("id", "keyword")  # 搜索框定位器
    # search_btn_loc = ("class name", "go")  # 搜索按钮定位器
    # text = "手机"
    # base.send_keys(search_loc, text)
    base1 = Shopping(driver)
    base1.click_portable_source()  # 点击移动电源
    base1.click_portable_battery()  # 点击充电宝
    base1.click_purchase()  # 立即购买
    time.sleep(2)
    # base.click(search_btn_loc)
    base1.click_delete()   # 点击删除按钮
    time.sleep(2)
    base.get_alert_cancel()   # 点击取消
    base.close()
