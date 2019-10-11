from flask import Blueprint


auth_bp = Blueprint('auth', __name__,
                    template_folder='templates',
                    static_folder='static')




@auth_bp.route('/')
def auth():
	return "This is Auth page"