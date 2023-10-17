from flask import Blueprint, redirect, url_for, render_template, request
lab3 = Blueprint ('lab3', __name__)

@lab3.route ('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route ('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    age = request.args.get('age')
    if user == '':
        errors[user] = 'Заполните поле пожалуйста !'
    elif age == '':
        errors[age] = 'Заполните поле пожалуйста !'
        
    sex = request.args.get('sex')
    return render_template('form1.html', user = user, age = age, sex = sex, errors = errors)

@lab3.route ('/lab3/order')
def order():
    return render_template('order.html')

@lab3.route ('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 10
    if request.args.get('sugar') == 'on':
        price += 30
    if request.args.get('salt-caramel') == 'on':
        price += 50

    return render_template('pay.html', price = price)

@lab3.route ('/lab3/success')
def succs():
    return render_template('success.html')

@lab3.route ('/lab3/bilet')
def bilett():
    ERERER = {}
    FIO = request.args.get('FIO')
    age = request.args.get('age')
    PA = request.args.get('PA')
    PB = request.args.get('PB')
    if FIO == '':
        ERERER[FIO] = 'Заполните поле пожалуйста !'
    elif age == '':
        ERERER[age] = 'Заполните поле пожалуйста !'
    elif PA == '':
        ERERER[PA] = 'Заполните поле пожалуйста !'
    elif PB == '':
        ERERER[PB] = 'Заполните поле пожалуйста !'
    
    
    return render_template('bilet.html', ERERER = ERERER, FIO = FIO, age = age, PA = PA, PB = PB)

@lab3.route ('/lab3/successb')
def succsss():
    return render_template('successb.html' )