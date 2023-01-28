import os
import json
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
    return render_template("index.html", page_title="Home")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact Us")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)


# Remove Debug mode parameter for production
