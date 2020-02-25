from os import getenv
from pymongo import MongoClient
from src.config.logger import Logger

import os

class Database:

    def connect(self):  
        logger = Logger()
        host = os.getenv("MONGO_HOST")
        port = os.getenv("MONGO_PORT")
        username = os.getenv("MONGO_USER")
        password = os.getenv("MONGO_PASS")
        db = os.getenv("MONGO_DB")
        return MongoClient(
                "mongodb://{}:{}@{}:{}/?authSource={}".format(username, password, host, port, db)
        )[db]
