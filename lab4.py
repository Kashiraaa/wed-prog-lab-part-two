from flask import Blueprint, redirect, url_for, render_template, request
lab4 = Blueprint ('lab4', __name__)

@lab4.route ('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route ('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html') 


    username = request.form.get ('username')
    password = request.form.get ('password')
    if username == 'alex' and password == '123':
        return render_template('success_lab4.html')


    if username == '' or username != 'alex' or password == '' or password != '123':
        error = 'Неверный логин и/или пароль'
        return render_template ('login.html', error = error)
    
@lab4.route('/lab4/cold', methods=['GET', 'POST'])
def holodos():
    if request.method == 'GET':
        return render_template('cold.html')

    temp = request.form.get('temp')
    error = ''
    msg = '' 
    sf = '' 

    if temp is None or temp == '':
        error = 'Ошибка: не задана температура'
    elif int(temp) < -12:
        error = 'не удалось установить температуру — слишком низкое значение'
    elif int(temp) > -1:
        error = 'не удалось установить температуру — слишком высокое значение'
    elif -12 <= int(temp) <= -9:
        msg = f'Установлена температура: {temp}°C'
        sf = '❄️❄️❄️'
    elif -8 <= int(temp) <= -5:
        msg = f'Установлена температура: {temp}°C'
        sf = '❄️❄️'
    elif -4 <= int(temp) <= -1:
        msg = f'Установлена температура: {temp}°C'
        sf = '❄️'

    return render_template('cold.html', error=error, temp=temp, msg=msg, sf=sf)
  
@lab4.route('/lab4/zr', methods=['GET', 'POST'])
def zerna():
    if request.method == 'GET':
        return render_template('zr.html')

    error = {}
    zr = request.form.get('zr')
    vs = request.form.get('vs')
    msgg = ''

    if vs is None or vs == '':
        error['vs'] = 'не введен вес'
    elif float(vs) <= 0:
        error['vs'] = 'неверное значение веса'
    elif zr:
        if zr == 'yachmen':
            pr = 12000 
        elif zr == 'oves':
            pr = 8500
        elif zr == 'psheniza':
            pr = 8700
        elif zr == 'roj':
            pr = 14000
        
    tc = float(vs) * pr

    if float(vs) > 50:
        tc *= 0.9
        msgg = 'Заказ успешно сформирован. Вы заказали зерно. Вес: {} т. Сумма к оплате: {} &#x20bd Применена скидка за большой объем.'.format(vs, tc)
    else:
        msgg = 'Заказ успешно сформирован. Вы заказали зерно. Вес: {} т. Сумма к оплате: {} &#x20bd'.format(vs, tc)

    if float(vs) > 500:
        msgg = 'Такого объема сейчас нет в наличии.'

    return render_template('zr.html', error=error, zr=zr, vs=vs, msgg=msgg)   