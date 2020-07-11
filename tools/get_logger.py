# 导包
import logging.handlers
from config import BASE_PATH
import os

# 定义类
class GetLogger:
    # 定义日志器变量
    __logger = None
    # 获取日志器方法
    @classmethod
    def get_logger(cls):
        # 判断日志器为空：
        if cls.__logger is None:
            # 获取日志器
            cls.__logger = logging.getLogger()
            # 设置日志器默认级别
            cls.__logger.setLevel(logging.INFO)
            # 获取处理器
            file_path = BASE_PATH + os.sep + "log" + os.sep + "hmtt.log"
            th = logging.handlers.TimedRotatingFileHandler(filename=file_path,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s %(funcName) %(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器中
            th.setFormatter(fm)
            # 将处理器添加到日志器中
            cls.__logger.addHandler(th)
        # 返回 日志器
        return cls.__logger
if __name__ == '__main__':
    log = GetLogger.get_logger()
    log.info("错误为info级别")
    log.error("错误为error级别")