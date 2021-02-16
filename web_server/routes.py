# API Routes
'''
# Features
- Add transaction
- View user balance
- View full record of transactions ordered by date
- Withdraw points from all users
'''
import json
from flask import jsonify, flash, redirect, request, abort, Response
from web_server import app
from .database import insert_transaction, spend_points, view_balance

# Adds a transaction given Payer's name, points, and timestamp 
@app.route("/api/user/transaction", methods=['PUT'])
def add_transaction():
    form = request.json
    payer = str(form['payer'])
    points = int(form['points'])
    timestamp = str(form['timestamp'])

    insert_transaction(payer, points, timestamp)
    return Response('{"message":"Transaction Added"}', status=202)

# Redeem points for a reward
@app.route("/api/user/redeem", methods=['PUT'])
def redeem_points():
    form = request.json
    points = int(form['points'])
    # TODO: Call to Database to deduct the points from the balance
    usage = spend_points(points)
    # Return a list of jsons of each user's deducted value
    usage_json = json.dumps(usage)
    # return Response('{"message":"Spent ' + str(points) + ' points"}', status=202)
    return usage_json

# Retrieve the user's balance
@app.route("/api/user/balance", methods=['GET'])
def check_balance():
    # Returns a list of all remaining balances from user transactions.
    balances = view_balance()
    # return Response('{"message":"Remaining Balance"}', status=200)
    balances_json = json.dumps(balances)
    return balances_json