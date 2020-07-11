from selenium import webdriver
#导包appium
import appium.webdriver
import page
from time import sleep

class GetDriver:
    # 1. 声明变量
    __web_driver = None

    # 声明app中driver变量
    __app_driver = None

    # 2. 获取driver方法
    @classmethod
    def get_web_driver(cls, url):
        # 判断是否为空
        if cls.__web_driver is None:
            # 获取浏览器
            cls.__web_driver = webdriver.Chrome()
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开url
            cls.__web_driver.get(url)
        # 返回driver
        return cls.__web_driver
    # 3. 退出driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            # 退出操作
            cls.__web_driver.quit()
            # 置空操作 重点
            cls.__web_driver = None

    # 获取app应用driver
    @classmethod
    def get_app_driver(cls):
        # 判断__app_driver为空
        if cls.__app_driver is None:
            # 设置启动
            desired_caps = {}
            # 设备信息，必填且正确
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            # 不为空即可
            desired_caps['deviceName'] = '127.0.0.1:62001'
            # 添加参数 automationName=UiAutomator1
            desired_caps['automationName'] = 'UiAutomator1'
            desired_caps['unicodeKeyboard'] = 'true'
            desired_caps['resetKeyboard'] = 'true'

            # app包名
            desired_caps['appPackage'] = page.appPackage
            # app启动名
            desired_caps['appActivity'] = page.appActivity
            # 设置driver
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 返回 cls.__app_driver
        return cls.__app_driver

    # 退出app应用driver
    @classmethod
    def quit_app_driver(cls):
        # 判断不为空
        if cls.__app_driver:
            # 退出操作
            cls.__app_driver.quit()
            # 置空操作
            cls.__app_driver = None

if __name__ == '__main__':
    GetDriver.get_app_driver()
    sleep(2)
    GetDriver.quit_app_driver()