from flask import Flask, render_template
from demo_app.admin import admin_bp
from demo_app.auth import auth_bp
from demo_app.home import home_bp

app = Flask(__name__)
# app.register_blueprint(admin_bp,url_prefix='/admin')
app.register_blueprint(admin_bp,url_prefix='/admin')
app.register_blueprint(auth_bp,url_prefix='/auth')
app.register_blueprint(home_bp,url_prefix='/home')


@app.route('/')
def index():
	return render_template("index.html")
	