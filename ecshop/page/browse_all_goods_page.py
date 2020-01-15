from common.base import Base


class Browse_all_goods_Page(Base):
    goods_loc = ("css selector", "div.goodsItem>a>img")
    search_loc = ("class name", "go")
    next_page_loc = ("link text", "下一页")

    def click_search(self):
        """点击搜索按钮"""
        self.click(self.search_loc)

    def get_element_alt_name(self):
        """获取所有商品元素的alt属性"""
        goods_elements = self.find_elements(self.goods_loc)
        alts = []
        for good_element in goods_elements:
            alt = good_element.get_attribute("alt")
            alts.append(alt)
        return alts

    def click_all_goods(self):
        """点击所有商品"""
        alts = self.get_element_alt_name()
        for alt in alts:
            goods_loc = ("css selector", f"img[alt='{alt}']")  # 重写定位器

            self.click(goods_loc)
            self.back()

    def is_next_page(self):
        """判断是否有下一页"""
        text = "下一页"
        while True:
            result = self.is_text_in_element(self.next_page_loc, text)
            if result:
                self.click(self.next_page_loc)
                self.get_element_alt_name()
                self.click_all_goods()
            else:
                return True


if __name__ == '__main__':
    from common.base import open_browser

    driver = open_browser()
    browser = Browse_all_goods_Page(driver)  # 实例化
    url = "http://localhost:8080/ecshop"
    browser.open_url(url)
    browser.click_search()
    browser.get_element_alt_name()
    browser.click_all_goods()
    browser.is_next_page()
