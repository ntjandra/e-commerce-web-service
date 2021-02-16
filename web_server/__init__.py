import os
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'notarealproductionkey'

# Create stored in-memory database
# conn = sqlite3.connect(':memory:')
# Note: Using the run.py separates the threads, sqlite doesn't like this,
# but it's safe since each transaction uses it's own cursor
conn = sqlite3.connect('test.db', check_same_thread=False)


from web_server import routes