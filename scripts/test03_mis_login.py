import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_logger import GetLogger
from tools.read_yaml import read_yaml

log = GetLogger.get_logger()
class TestMisLogin:
    # 初始化
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_web_driver(page.url_mis)
        # 2. 通过统一入口类获取PageMisLogin
        self.mis = PageIn(driver).page_get_PageMisLogin()
    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_web_driver()
    # 登录测试业务方法
    @pytest.mark.parametrize("username, pwd, expect", read_yaml("mis_login.yaml"))
    def test_mis_login(self, username, pwd, expect):
        # 1. 调用登录业务方法
        self.mis.page_mis_login(username, pwd)
        try:
            # 2. 断言信息
            assert expect in self.mis.page_get_nickname()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.mis.base_get_img()
            # 抛异常
            raise