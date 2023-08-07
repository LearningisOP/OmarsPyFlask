from flask import Flask;
from flask import request, url_for, make_response;
from blueprints.passwordgenerator.randompasswordgen import randompasswordgen_bp
from blueprints.login_page.login import login_bp
from blueprints.main_page.about import about_bp
from blueprints.some_pics.img_grid import img_grid_bp

app = Flask(__name__)

# register blueprints
app.register_blueprint(about_bp, static_folder='main_page/static')

app.register_blueprint(login_bp, url_prefix="/login")

app.register_blueprint(randompasswordgen_bp, url_prefix="/PGen",static_folder='passwordgenerator/static')

app.register_blueprint(img_grid_bp, url_prefix="/picgrid")



#! once you deploy your app remove the following two lines or set debug = to false
if __name__ == '__main__':
    app.run(debug=True)