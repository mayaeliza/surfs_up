from flask import Flask 

# create a new app
app = Flask(__name__) 

# create flask routes
@app.route('/')
def hello_world():
    return 'Hello world'