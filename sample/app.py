from flask import Flask, jsonify , Request, Response,redirect
from  ..app import UniAuth as Auth
import os
app = Flask(__name__)
uniAuth = Auth([{
    "name": 'server1',
    "url": 'http://localhost:5000',
    "clientId": '6032634dd05be80880499244',
    "clientSecret": '336fe562-33bf-4448-b87d-d17105eabb25',
    "redirectUri": 'www.facebook.com',
    # "processor": def processor(profile: str, next): 
    #                 print('received user profile > ', profile);
    #                 next();
    
    "endpoint": {
      'auth': 'account/o/login',
      'profile': 'account/o/access',
    },
}])




@app.route('/')
def homepage():
    data = {
        "alive" : True,
        "login" : 'open /login to initiate auth'
    }
    return jsonify(data)

@app.route('/login')
def login():
    loginUrl = uniAuth.authenticate('server1',)
    return redirect(loginUrl)

@app.route('/callback')
def cbk():
    uniAuth.callback('server1')
    return jsonify('user logged in')
        

if __name__=='__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='localhost', port=port)
