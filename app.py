from flask import Flask

# Create a flask app instance. 
app = Flask(__name__)

# Create the route
@app.route('/')
def hello_world():
 return 'Hello world'

