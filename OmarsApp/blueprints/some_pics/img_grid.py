from flask import Blueprint, render_template, request, redirect, url_for, make_response


img_grid_bp = Blueprint('img_grid', __name__, template_folder="templates", 
                        static_folder='static', static_url_path='some_pics')


@img_grid_bp.route("/")
def images():
    if request.authorization and request.authorization.username == 'images' and request.authorization.password == 'w3lcome':
        return render_template("img_grid.html")
    return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

