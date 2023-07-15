from flask import Blueprint, render_template,request, redirect, url_for


login_bp = Blueprint('login', __name__, template_folder="templates")


@login_bp.route("/sign-up")
def loginindex():
    return render_template("login.html")


