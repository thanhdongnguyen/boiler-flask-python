'''
    @author: dongnt
    Server Config
'''
from src.helpers.timer import Timer
from dotenv import load_dotenv

import os

load_dotenv(dotenv_path="/src/.env")
date = Timer.get_current_format()
file_name = "{}/flask_teamate_{}.log".format("/src/logs", date)


HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
bind = "{}:{}".format(HOST, PORT)

backlog = 2048

workers=3
worker_class="sync"
worker_connections=1000
timeout=15
keepalive=1

spew = False 

reload = True

daemon=False
#pidfile=/tmp/hackathon.pid
umask=0
user=None
group=None
logfile=file_name
