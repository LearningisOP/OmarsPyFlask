from flask import Blueprint, render_template, request, redirect, url_for


img_grid_bp = Blueprint('img_grid', __name__, template_folder="templates", 
                        static_folder='static', static_url_path='some_pics')


@img_grid_bp.route("/")
def images():
    return render_template("img_grid.html")

