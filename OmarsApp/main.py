from flask import Flask , request, url_for
from blueprints.passwordgenerator.randompasswordgen import randompasswordgen_bp
from blueprints.main_page.about import about_bp

app = Flask(__name__)

# register blueprints
app.register_blueprint(randompasswordgen_bp, url_prefix="/PGen",static_folder='passwordgenerator/static')

app.register_blueprint(about_bp)

#test latet import genpasswordapp.py

#! once you deploy your app remove the following two lines or set debug = to false
if __name__ == '__main__':
    app.run(debug=True)