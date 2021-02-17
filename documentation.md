# e-commerce web-service
## Using the web-service

### Start up web server
1. Open a terminal and git clone the repository
2. In the main branch, root directory, type ```python3 run.py```
By default this is set to run on localhost:5000
Now the server is up and users may call the endpoints

## Call endpoints

### Gain Points
Send a PUT request to ```http://localhost:5000/api/user/transaction``` to earn points
It accepts JSONs with the <payer>, <points>, and <timestamp> the transaction occured.

### Redeem points
Send a PUT request to ```http://localhost:5000/api/user/redeem``` to redeem points
It accepts JSONs with the <points> to be subtracted from your account.


### Check total points
Send a GET request to ```http://localhost:5000/api/user/balance``` to see your detailed balance and the payer who sent them.
The caller recieves a JSON of the <payer> and <points> 

### Known bugs
Bugs are outlined in [#issue](https://github.com/ntjandra/e-commerce-web-service/issues)
