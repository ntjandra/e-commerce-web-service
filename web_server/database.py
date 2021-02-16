# Experimenting with SQLite3
# from web_server import conn
import sqlite3

conn = sqlite3.connect('test.db')

# Create a Table that has payer (string), points (integer), timestamp (date).
# Note: SQLite3 stores dates as TEXT since it lacks a date datatype
def init_db():
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                (payer text, points integer, timestamp text)''')
    # Save (commit) the changes
    conn.commit()

def show_db():
    c = conn.cursor()
    c.execute('''SELECT * FROM transactions''')
    print(c.fetchone())

# Initial Assumption: Timestamp is pre-formated correctly 
def insert_transaction(payer, points, timestamp):
    c = conn.cursor()
    record = (payer, points, timestamp)
    print("Inserting", record)
    c.execute('''INSERT INTO transactions VALUES (?,?,?)''', record)

init_db()
insert_transaction("Nathan", 5000, "2020-11-02T14:00:00Z")
show_db()