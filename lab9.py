from flask import Blueprint, render_template

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def main():
    return render_template('/lab9/index.html')

@lab9.app_errorhandler(404)
def not_found(e):
    return render_template('/lab9/error.html'), 404

@lab9.app_errorhandler(500)
def internal_server_error(error):
    return render_template('/lab9/error500.html'), 500

@lab9.route('/lab9/500')
def trigger_error():
    a = 1 / 0
    return 'This will not be executed'