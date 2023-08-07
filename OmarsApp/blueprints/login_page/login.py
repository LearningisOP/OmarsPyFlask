from flask import Blueprint, render_template, request, redirect, url_for


login_bp = Blueprint('login', __name__, template_folder="templates")


@login_bp.route("/")
def login():
    return render_template("login.html")


@login_bp.route("/register", methods=['POST'])
def register():
    name = request.form.get("name")
    forfun = request.form.get("forfun")
    personalReason = request.form.get("personalReason")
    Curiosity = request.form.get("Curiosity")
    Other = request.form.get("Other")
    return render_template("about.html")



