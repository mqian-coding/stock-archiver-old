from flask import Flask

PORT = 8000
server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

# Used to get all the routes
from .routes import *
