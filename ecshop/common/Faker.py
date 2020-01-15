from faker import Faker, Factory

fake = Faker("zh_CN")


# print(fake.name)


class Faker_data:
    # faker类生成随机填写信息
    def faker_user(self):
        """随机用户名"""
        user = fake.user_name()
        return user

    def faker_password(self):
        """随机密码"""
        pd = fake.password()
        return pd

    def faker_email(self):
        """随机邮件"""
        email = fake.email()
        return email

    def faker_qq(self):
        """随机qq号码"""
        qq = fake.random_int(min=0, max=9999999999)
        return qq

    def faker_tel(self):
        """随机电话号码"""
        tel = fake.phone_number()
        return tel

    def faker_pro(self):
        """随机问题答案"""
        pro = fake.word()
        return pro

    def faker_add(self):
        """随机收货地址"""
        add = fake.address()
        return add

    def faker_post(self):
        post = fake.postcode()
        return post

# def create_names():
# fake = Factory.create()
# print(dir(fake))


if __name__ == '__main__':
    from common.base import open_browser
    from page.registerpage import RegisterPage
    import time

    driver = open_browser("chrome")
    register = RegisterPage(driver)

    url = "http://localhost:8080/ecshop/index.php"  # ecshop商城地址
    register.open_url(url)
    time.sleep(2)

    print(Faker_data().faker_email())
    # print(Faker_data().faker_pro())
    # print(Faker_data().faker_qq())
    # print(Faker_data().faker_tel())
    # print(Faker_data().faker_user())
