from flask import Blueprint, render_template, request

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


@lab9.route('/lab9/input_card', methods=["GET"])
def input_card():
    return render_template('/lab9/input.html')

@lab9.route('/lab9/card', methods=['GET'])
def card():
    recipient_name = request.args.get('recipientName')
    recipient_gender = request.args.get('recipientGender')
    sender_name = request.args.get('senderName')
    message = request.args.get('message')
    return render_template('/lab9/card.html', recipient_name=recipient_name, recipient_gender=recipient_gender,
                           sender_name=sender_name, message=message)