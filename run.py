import os
from flask import Flask, render_template
# Import  the flask class from the flask module

app = Flask(__name__)
# Defining an instance of the flask class with the name
#  of the applications module as the parameter
# (__name is a built in variable that returns
#  the name of the module python module)


# decorator is wrapping the function and adding functionality to it
# when someone hits the / endpoint, the function index() will be called

# Each of these is a view attached to a route, rendering a page
# In the HTML files the function is called to
#  get the file (using {{url_for('filename')}})


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)


# Remove Debug mode parameter for production
