import pytest

from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_logger import GetLogger
from tools.read_yaml import read_yaml

log = GetLogger.get_logger()
class TestAppLogin:
    # 1. 初始化
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_app_driver()
        # 2. 调用统一入口类PageAppLogin对象
        self.login = PageIn(driver).page_get_PageAppLogin()

    # 2. 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_app_driver()

    # 3. 登录app业务测试方法
    @pytest.mark.parametrize("phone, code", read_yaml("app_login.yaml"))
    def test_app_login(self, phone, code):
        # 调用登录app业务方法
        self.login.page_app_login(phone, code)
        try:
            # 断言
            assert self.login.page_is_login_success()
        except Exception as e:
            # 1. 日志
            log.error(e)
            # 2. 截图
            self.login.base_get_img()
            # 3. 抛异常
            raise