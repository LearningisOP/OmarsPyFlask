from flask import Blueprint, render_template,request, redirect, url_for


login_bp = Blueprint('login', __name__, template_folder="templates")


@login_bp.route("/sign-up", methods=['GET', 'POST'])
def loginindex():
    return render_template("signup.html")

@login_bp.route("/login", methods=['GET', 'POST'])
def loginindex():
    return render_template("login.html")


@login_bp.route("/logout", methods=['GET', 'POST'])
def loginindex():
    return redirect(url_for("views.html"))


