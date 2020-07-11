import page
from time import sleep

from base.web_base import WebBase
from tools.get_logger import GetLogger

log = GetLogger.get_logger()
class PageMpLogin(WebBase):
    # 输入用户名
    def page_input_username(self, username):
        # 调用父类中输入方法
        self.base_input(page.mp_username, username)

    # 输入验证码
    def page_input_code(self, code):
        # 调用父类中输入方法
        self.base_input(page.mp_code, code)

    # 点击登录按钮
    def page_click_login_btn(self):
        # 调用父类中点击方法
        sleep(1)  # 解决电脑反应快的问题
        self.base_click(page.mp_login_btn)

    # 获取昵称封装 -> 测试脚本层断言使用
    def page_get_nickname(self):
        # 调用父类中获取文本方法
        return self.base_get_text(page.mp_nickname)

    # 组合业务方法 -> 测试脚本层调用
    def page_mp_login(self, username, code):
        log.info("正在调用自媒体登录业务方法，用户名：{}，验证码：{}".format(username, code))
        """提示：调用相同页面操作步骤，跨页面暂时不考虑"""
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()
    # 组合业务方法 -> 发布文章调用
    def page_mp_login_success(self, username="13812345678", code="246810"):
        log.info("正在调用自媒体登录业务方法，用户名：{}，验证码：{}".format(username, code))
        """提示：调用相同页面操作步骤，跨页面暂时不考虑"""
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()