from flask import Blueprint, render_template, request, redirect, url_for

about_bp = Blueprint('about', __name__, template_folder="templates", static_url_path='/main_page/static', static_folder='static')



@about_bp.route("/aboutme")
def aboutmepage():
    return render_template("about.html")

@about_bp.route("/")
def home():
    return render_template("home.html")

