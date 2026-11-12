import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] (%(name)s) -  %(filename)s - %(funcName)s %(message)s - %(lineno)d",
    filename="less.log",
    filemode="a"
)


logging.debug("Это отладочное сообщение!")
logging.info("Это информационное сообщение!")


def demo():
    logging.warning("Это предупреждение!")


demo()

logging.error("Это сообщение об ошибке!")
logging.critical("Это критическое сообщение!")