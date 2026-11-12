import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] (%(name)s) -  %(filename)s - %(funcName)s %(message)s - %(lineno)d",
    # filename="less.log",
    # filemode="a"
)


logger_main = logging.getLogger("main")
logger_data = logging.getLogger("data")


logger_main.debug("Это отладочное сообщение!")
logger_data.info("Это информационное сообщение!")


def demo():
    logger_main.warning("Это предупреждение!")


demo()

logger_data.error("Это сообщение об ошибке!")
logger_data.critical("Это критическое сообщение!")