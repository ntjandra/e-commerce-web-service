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
def spend_points(points):
    c = conn.cursor()

    # Keep track of individual's spending
    clients = {}
    usage = {}

    # Get first 
    c.execute('''SELECT payer, points FROM transactions ORDER BY timestamp ASC''')
    result = c.fetchone()
    while result != None:
        payer, owned_points = result

        # Check if the payer is new.
        if payer not in clients:
            clients[payer] = points
            usage[payer] = 0

        # subtract result with points until the value is zero.
        if owned_points > clients[payer]:
            spent_points = owned_points - clients[payer]
            clients[payer] -= spent_points
            usage[payer] += spent_points
        else:
            # Don't have enough points
            # Deduct remainer into spent
            usage[payer] += clients[payer]
            clients[payer] = 0

        # Grab next transaction
        result = c.fetchone()
    
    # at the end return the amount spent
    return clients

### Test 1: Insertion
init_db()
insert_transaction("Nathan", 5000, "2020-11-02T14:00:00Z")
insert_transaction("DANNON", 1000, "2020-11-02T14:00:00Z")
insert_transaction("UNILEVER", 200,"2020-10-31T11:00:00Z")
insert_transaction("DANNON", -200, "2020-10-31T15:00:00Z")
insert_transaction("MILLER COORS", 10000, "2020-11-01T14:00:00Z")
insert_transaction("DANNON", 300, "2020-10-31T10:00:00Z")
show_db()

### Test 2: Update, based on Redemption
spend_points(5000)
show_db