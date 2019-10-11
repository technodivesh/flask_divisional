from flask import Blueprint


admin_bp = Blueprint('admin', __name__,
                    template_folder='templates',
                    static_folder='static')




@admin_bp.route('/')
def admin():
	return "This is admin page"



@admin_bp.route('/detail')
def detail():
	return "This is admin detail page"
