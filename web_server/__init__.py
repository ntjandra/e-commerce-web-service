import os
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .database import init_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'notarealproductionkey'

# Create stored in-memory database
# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('test.db')

from web_server import routes