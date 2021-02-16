# Driver File that runs the api as a simple service
from web_server import app
# Get the App and Run it from init.py
if (__name__) == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')