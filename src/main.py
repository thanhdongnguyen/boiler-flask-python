# -*- encoding: utf-8 -*-

from flask import Flask, g as global_context, jsonify, request
from .routes import Routes
from src.helpers.message import Message
from src.helpers.jwt import JWT
from src.config.logger import Logger
from src.config.database import Database
from src.config.cache import Cache

import os

app = Flask(__name__)
logger = Logger()

@app.before_request
def before_request():
    
    database = Database()
    global_context.db = database.connect()

@app.after_request
def after_request(response):
    #global_context.db.close()


    '''
        Add response header to fix error CORS
    '''
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "client-authorization"
    return response

@app.errorhandler(Exception)
def errorhandler(error):
    logger.exception(error)
    return Message.error(99)


router = Routes(app)
router.v1()
