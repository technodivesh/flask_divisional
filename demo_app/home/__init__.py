from flask import Blueprint, redirect, url_for


home_bp = Blueprint('home', __name__,
                    template_folder='templates',
                    static_folder='static')




@home_bp.route('/')
def home():
	return "This is Home page"


@home_bp.route('/about')
def about():
	return "hiiiiiii"
	return redirect(url_for('home'))

