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

    # Keep track of individual's spending
    usage = {}

    # Get first 
    c.execute('''SELECT payer, points FROM transactions ORDER BY timestamp ASC''')
    result = c.fetchone()
 
    # Stop when transaction cannot be fufilled or finished spending points
    while (result != None) and (owed_points > 0):
        payer, owned_points = result
        print(payer, owned_points)
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
 
        # Grab next transaction
        result = c.fetchone()
        print(result)
    print(payer, owned_points, usage[payer])
    # at the end return the amount spent

    # Using these new values, we can safety add the redemption as a transaction.
    return usage

### Test 1: Insertion
init_db()
insert_transaction("Nathan", 5000, "2020-11-02T14:00:00Z")
insert_transaction("DANNON", 1000, "2020-11-02T14:00:00Z")
insert_transaction("UNILEVER", 200,"2020-10-31T11:00:00Z")
insert_transaction("DANNON", -200, "2020-10-31T15:00:00Z")
insert_transaction("MILLER COORS", 10000, "2020-11-01T14:00:00Z")
insert_transaction("DANNON", 300, "2020-10-31T10:00:00Z")
# show_db()

### Test 2: Update, based on Redemption
spent = spend_points(5000)
print("Redeemed", spent)
# show_db()