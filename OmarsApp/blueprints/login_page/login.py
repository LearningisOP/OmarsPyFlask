from flask import Blueprint, render_template, request, redirect, url_for, flash


login_bp = Blueprint('login', __name__, template_folder="templates")

REGISTRANTS = {}

REASONS = [
    "Curiosity"
    "personalReason"
    'forfun'
]


@login_bp.route("/")
def login():
    return render_template("login.html", reason=REASONS)


@login_bp.route("/register", methods=['POST'])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("login.html")
    reason = request.form.get("reason")
    Other = request.form.get("otherRad")
    if reason not in REASONS:
        return render_template("login.html")
    return render_template("about.html")


@login_bp.route("/registered")
def registered():
    return render_template("registrants.html")



