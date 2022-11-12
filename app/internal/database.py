import os

from mongoengine import connect
from dotenv import load_dotenv

from .logger import Logger

load_dotenv()


class DatabaseConfig:

    logger = Logger(__name__)

    def connect_database(self):
        connection_string = os.getenv('MONGODB_URI')
        connect(host=connection_string)
        self.logger.info({'message': "Database Online"})
