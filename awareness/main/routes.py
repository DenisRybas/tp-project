from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/faq")
def faq():
    return render_template("faq.html")


@main.route("/contacts")
def contacts():
    return render_template("contacts.html")
