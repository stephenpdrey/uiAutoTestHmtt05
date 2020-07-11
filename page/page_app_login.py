from base.app_base import AppBase
import page
from time import sleep
from tools.get_logger import GetLogger

log = GetLogger.get_logger()
class PageAppLogin(AppBase):
    # 1. 输入手机号
    def page_input_phone(self, phone):
        self.base_input(page.app_phone, phone)
    # 2. 输入验证码
    def page_input_code(self, code):
        self.base_input(page.app_code, code)
    # 3. 点击登录
    def page_click_login_btn(self):
        # 建议等待1-2秒
        sleep(2)
        self.base_click(page.app_login_btn)
    # 4. 判断是否存在指定元素 我的
    def page_is_login_success(self):
        sleep(2)
        return self.app_base_is_exist(page.app_my)
    # 5. 组合App登录业务测试方法
    def page_app_login(self, phone, code):
        log.info("正在调用app登录页面业务方法，手机号：{}，验证码：{}".format(phone, code))
        self.page_input_phone(phone)
        self.page_input_code(code)
        self.page_click_login_btn()

    # 6. 组合App登录成功依赖业务测试方法
    def page_app_login_success(self, phone="13812345678", code="246810"):
        log.info("正在调用app登录成功页面业务方法，手机号：{}，验证码：{}".format(phone, code))
        self.page_input_phone(phone)
        self.page_input_code(code)
        self.page_click_login_btn()