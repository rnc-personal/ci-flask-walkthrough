import os
from flask import Flask
# Import  the flask class from the flask module

app = Flask(__name__)
# Defining an instance of the flask class with the name of the applications module as the parameter
# (__name is a built in variable that returns the name of the module python module)


# decorator is wrapping the function and adding functionality to it
# when someone hits the / endpoint, the function index() will be called
@app.route("/")
def index():
    return "Hello, World"

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)