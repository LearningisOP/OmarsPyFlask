from flask import Blueprint, render_template, request, redirect, url_for


login_bp = Blueprint('login', __name__, template_folder="templates")


@login_bp.route("/sign-up", methods=['GET', 'POST'])
def signup():
    username = request.form.get("username")
    print(username)
    return render_template("signup.html")

@login_bp.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@login_bp.route("/logout", methods=['GET', 'POST'])
def logout():
    return redirect(url_for("views.html"))


