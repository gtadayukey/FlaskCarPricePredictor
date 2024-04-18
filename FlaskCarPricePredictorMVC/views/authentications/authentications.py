from flask import Blueprint, render_template, redirect, url_for

authentications_bp = Blueprint("authentications", __name__, template_folder="templates")


@authentications_bp.route("/")
def index():
    return redirect(url_for('authentications.login'))


@authentications_bp.route("/login")
def login():
    return render_template("login.html")


@authentications_bp.route("/register")
def register():
    return render_template("register.html")
