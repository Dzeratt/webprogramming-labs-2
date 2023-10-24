from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле'
    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    return render_template('success.html')


@lab3.route('/lab3/tiketsorder')
def tiketsorder():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле'

    return render_template('tiketsorder.html', user=user, errors=errors)

@lab3.route('/lab3/ticket')
def ticket():
    user = request.args.get('user')
    type = request.args.get('type')
    place = request.args.get('place')
    baggage = request.args.get('baggage')
    age = request.args.get('age')
    pv = request.args.get('pv')
    pn = request.args.get('pn')
    date = request.args.get('datetime')
    return render_template('ticket.html', user=user, type=type, place=place, baggage=baggage, age=age, pv=pv, pn=pn, date=date)