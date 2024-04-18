from flask import Blueprint, render_template, redirect, url_for

home_bp = Blueprint("index", __name__, template_folder="templates")


@home_bp.route("/home")
def home():
    return render_template("home.html")


@home_bp.route("/privacy")
def privacy():
    return render_template("privacy.html")
