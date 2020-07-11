from base.app_base import AppBase
import page
from tools.get_logger import GetLogger

log = GetLogger.get_logger()
class PageAppArticle(AppBase):
    # 1. 查找频道
    def page_click_channle(self, click_text):
        # 调用从右向左滑动方法
        self.app_base_right_wipe_left(page.app_channel_area, click_text)
    # 2. 查找文章
    def page_click_article(self, title):
        self.app_base_down_wipe_up(page.app_article_area, click_text=title)
    # 3. 查找文章业务方法
    def page_app_article(self, find_text, title):
        log.info("正在调用查看文章业务方法，所属频道：{}，标题：{}".format(find_text, title))
        # 调用查找频道
        self.page_click_channle(find_text)
        # 调用查找文章
        self.page_click_article(title)