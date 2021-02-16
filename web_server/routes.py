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
@app.route("/api/user/add", methods=['PUT'])
def add_transaction():
    form = request.json
    payer = str(form['payer'])
    points = int(form['points'])
    timestamp = str(form['timestamp'])
    # TODO: Replace with the DB call/action
    # print(payer, points, timestamp)
    return Response('{"message":"Transaction Added"}', status=202)
