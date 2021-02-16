# Experimenting with SQLite3
# from web_server import conn
import sqlite3
from datetime import datetime
from web_server import conn

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
    c.execute('''SELECT * FROM transactions ORDER BY timestamp DESC''')
    print("Fetch")
    print(c.fetchall())

# Initial Assumption: Timestamp is pre-formated correctly
def insert_transaction(payer, points, timestamp):
    c = conn.cursor()
    record = (payer, points, timestamp)
    print("Inserting", record)
    c.execute('''INSERT INTO transactions VALUES (?,?,?)''', record)

# Conditions: Point Value must never dip below zero
# Requirement: Deletion happens from oldest transaction
def spend_points(owed_points):
    c = conn.cursor()

    # Keep track of where the credits came from.
    usage = {}

    # Get first 
    c.execute('''SELECT payer, points FROM transactions ORDER BY timestamp ASC''')
    result = c.fetchone()
 
    # Stop when transaction cannot be fufilled or finished spending points
    while (result != None) and (owed_points > 0):
        payer, owned_points = result
        # Track which transactions to redeem.
        if payer not in usage:
            usage[payer] = 0

        # subtract result with points until the value is zero.
        if owed_points > owned_points:
            # Spend all the owned points
            owed_points -= owned_points
            # Log where the points came from
            usage[payer] -= owned_points
        else:
            # Own enough points
            usage[payer] -= owed_points
            owed_points = 0

        # Grab next transaction
        result = c.fetchone()

    # at the end return the amount spent
    # Using these new values, we can safely add each redemption as a transaction. (in the route)
    return usage

def view_balance():
    c = conn.cursor()

    # Keep track of where the credits came from.
    balance = {}
    # Get first 
    c.execute('''SELECT payer, points FROM transactions ORDER BY timestamp ASC''')
    result = c.fetchone()
 
    # Stop when out of transactions
    while result != None:
        payer, owned_points = result
        
        if payer not in balance:
            balance[payer] = 0

        balance[payer] += owned_points
        # Grab next transaction
        result = c.fetchone()

    return balance