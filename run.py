import os
# Built in OS module for anything server side essentially
import json
# Built in Json module for reading the compnaies file, which is liek a temp DB
from flask import Flask, render_template, request, flash
# Import the flask class from the flask module
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
# Defining an instance of the flask class with the name
# of the applications module as the parameter
# (__name__) is a built in variable that returns
# the name of the module python module
app.secret_key = os.environ.get("SECRET_KEY")
# Secret key is used for proteting the form data submitted on the contact page


"""
Routing
"""
# @app decorator is wrapping the function and adding functionality to it
# when someone hits the / endpoint, the function index() will be called

# Each of these is a view attached to a route, rendering a page
# In the HTML files the function is called to
#  get the file (using {{url_for('filename')}})


@app.route("/")
def index():
    return render_template("index.html", page_title="Home")
    # render_template is a flasjk function that goes and
    # finds the named file to render it
    # After the comma are additional varaibles we can pass 
    # to that page to use them there, like an export


@app.route("/about")
def about():
    # This page uses the json file so we create an empty object to store it in
    data = []
    with open("data/company.json", "r") as json_data:
        # We read the json file and store it as the json_data variable
        data = json.load(json_data)
        # assign the parsed json to the data variable
    return render_template("about.html", page_title="About", company=data)
    # we return the about template, pass the page title variable and
    # also the parsed data from the json file to that page


@app.route("/about/<member_name>")
# This is the individual, lowest level page for the json data returned
# the angle brackets denote that this is dynamic piece of data
def about_member(member_name):
    member = {}
    # Set an empty object to store each member
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            # we iterate through the loaded json data and if the url
            # in there matches the url the client is accessing
            # it will return the right page with the members name as
            # the slug from the <member_name> parameter above
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)
    # We need to pas the member variable to the apge for this routing to work


@app.route("/contact", methods=["GET", "POST"])
# This page contains a form so, we need to define some methods
# that can be used there. 
# These should always be the same really.
def contact():
    if request.method == "POST":
        # "If someone makes a post request"
        flash("Thanks {}, We received your message".format(
            request.form.get("name")))
# Use the flash method from Flask to read
# the contents of the form submission
    return render_template("contact.html", page_title="Contact Us")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
# These are boilerplate setup options telling python,
# Flask and heroku how to serve the site up
# They are used in Herokus ENV variables when thos are added (IP, PORT)
# Remove Debug mode parameter for production


