import os

from mongoengine import connect
from .logger import Logger


class DatabaseConfig:

    logger = Logger(__name__)

    def connect_database(self):
        connection_string = os.getenv('MONGODB_URI')
        connect(host=connection_string)
        self.logger.info({'message': "Database Online"})
