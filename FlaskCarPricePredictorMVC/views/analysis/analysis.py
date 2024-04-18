from flask import Blueprint, render_template

analysis_bp = Blueprint("analysis", __name__, template_folder="templates")


@analysis_bp.route("/")
def home():
    return render_template("home.html")
