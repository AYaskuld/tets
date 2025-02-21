import multiprocessing
from src.config.server import Server_conf

host="0.0.0.0"
port=int(Server_conf.SERVER_PORT)

bind = f"{host}:{port}"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
wsgi_app = "main:app"
threads = 2 
timeout = 30 
loglevel = "info"
accesslog = "-" 
errorlog = "-" 
daemon = False 
