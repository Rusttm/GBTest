import logging
from logging.handlers import RotatingFileHandler

class AnimalsLogger():
    logger_name = "animals"
    logger = None

    def __init__(self):
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(logging.DEBUG)
        if self.logger.hasHandlers(): self.logger.handlers.clear()
        logger_handler = RotatingFileHandler(f"{self.logger_name}.log", mode="a", backupCount=0,
                                             maxBytes=10 * 1024 * 1024, delay=0)
        # logger_handler = logging.FileHandler("controller.log", mode="w")
        logger_formatter = logging.Formatter("%(asctime)s,%(msecs)d %(name)s %(levelname)s msg: %(message)s")
        logger_handler.setFormatter(logger_formatter)
        self.logger.addHandler(logger_handler)


if __name__ == '__main__':
    connector = AnimalsLogger()
    connector.logger.info("resting")

