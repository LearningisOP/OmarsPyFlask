from flask import Blueprint, render_template, request, redirect, url_for, flash


login_bp = Blueprint('login', __name__, template_folder="templates", static_url_path='/login_page/static', static_folder='static')

REGISTRANTS = {}

REASONS = [
    "Business",
    "Curiosity",
    "Family/Friend",
    'for fun'
]

@login_bp.route("/")
def login():
    return render_template("LandingPage.html")


@login_bp.route("/register", methods=['POST'])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("login.html")
    reason = request.form.get("reason")
    Other = request.form.get("otherRad")
    if reason not in REASONS:
        return render_template("login.html")
    REGISTRANTS[reason] = reason
    return render_template("home.html")


@login_bp.route("/registered")
def registered():
    return render_template("registrants.html", registrants=REGISTRANTS)

@login_bp.route("/about")
def skip():
    return render_template("home.html")



