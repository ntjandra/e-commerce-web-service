# API Routes
'''
# Features
- Add transaction
- View user balance
- View full record of transactions ordered by date
- Withdraw points from all users
'''
from flask import jsonify, flash, redirect, request, abort, Response
from web_server import app

# Adds a transaction given Payer's name, points, and timestamp 
@app.route("/api/user/transaction", methods=['PUT'])
def add_transaction():
    form = request.json
    payer = str(form['payer'])
    points = int(form['points'])
    timestamp = str(form['timestamp'])
    # TODO: Replace with the DB call/action
    # print(payer, points, timestamp)
    return Response('{"message":"Transaction Added"}', status=202)

# Redeem points for a reward
@app.route("/api/user/redeem", methods=['PUT'])
def redeem_points():
    form = request.json
    points = int(form['points'])
    return Response('{"message":"Spent ' + str(points) + ' points"}')
    # TODO: Call to Database to deduct the points from the balance
    # Return a list of jsons of each user's deducted value
