from flask import Blueprint, render_template, request, redirect

about_bp = Blueprint('about', __name__, template_folder="templates")



@about_bp.route("/aboutme")
def aboutmepage():
    return render_template("about.html")

@about_bp.route("/")
def home():
    return render_template("index.html")

