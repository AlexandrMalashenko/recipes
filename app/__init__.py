from flask import Flask
from logging.handlers import RotatingFileHandler
import logging


app = Flask(__name__)

file_handler = RotatingFileHandler('logs.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

from app import routes
