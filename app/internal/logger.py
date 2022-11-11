import json
import logging


class Logger:

    def __init__(self, log_name):
        self.logger = self.get_logger(log_name)

    @staticmethod
    def get_logger(log_name) -> logging.Logger:

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

        logger = logging.getLogger(log_name)
        handler = logging.FileHandler('log_file.log')

        logger.addHandler(handler)
        handler.setFormatter(formatter)

        return logger

    def info(self, data):
        self.logger.info(json.dumps(data))

    def error(self, data):
        self.logger.error(json.dumps(data))
