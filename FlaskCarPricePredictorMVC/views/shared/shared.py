from flask import Blueprint, render_template

shared_bp = Blueprint("home", __name__, template_folder="templates")


@shared_bp.route("/error")
def home():
    return render_template("error.html")
