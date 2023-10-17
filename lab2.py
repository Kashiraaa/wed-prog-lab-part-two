from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint ('lab2', __name__)

@lab2.route ("/lab2")
def examp():
    name = 'Danil'
    numlab = '2'    
    numgroup = '14'
    numcorus = 'III'
    strstr= 'стр.'
    fruits=[
        {'name': 'яблоко', 'price': '100'},
        {'name': 'мандарин', 'price': '200'},
        {'name': 'слива', 'price': 'бесплатно'},
        {'name': 'груша', 'price': '145'},
        {'name': 'апельсин', 'price': '225'},
        {'name': 'граната', 'price': '451'}
        ]
    books=[
        {'autor': 'Л. Н. Толстой', 'srname': 'Война и мир', 'jnr': 'роман', 'str': '1300'},
        {'autor': 'А. С. Пушкин', 'srname': 'Капитанская дочка', 'jnr': 'Роман', 'str': '125'},
        {'autor': 'М. Ю. Лермонтов', 'srname': 'Герой нашего времени', 'jnr': 'Психологический реализм', 'str': '224'},
        {'autor': 'Ф. М. Достоевский', 'srname': 'Преступление и наказание', 'jnr': 'Криминалистика', 'str': '672'},
        {'autor': 'А. П. Чехов', 'srname': 'Пари', 'jnr': 'Рассказ', 'str': '250'},
        {'autor': 'И. С. Тургенев', 'srname': 'Отцы и дети', 'jnr': 'Политическая фантасика', 'str': '288'},
        {'autor': '	Н. В. Гоголь', 'srname': 'Мертвые души', 'jnr': 'Сатира', 'str': '352'},
        {'autor': 'М. Горький ', 'srname': 'Старуха Изергиль', 'jnr': 'Рассказ', 'str': '125'},
        {'autor': 'А. И. Куприн ', 'srname': 'Гранатовый браслет', 'jnr': 'Драма', 'str': '224'},
        {'autor': 'Н. А. Некрасов ', 'srname': 'Русские женщины', 'jnr': 'Поэма', 'str': '124'},
        {'autor': 'И. А. Бунин ', 'srname': 'Господин из Сан-Фарнциско', 'jnr': 'Рассказ', 'str': '128'}
        ]
    return render_template('example.html', name = name, numlab = numlab, 
                            numgroup = numgroup, numcorus = numcorus, 
                            fruits=fruits, books=books, strstr=strstr)


@lab2.route ("/lab2/")
def lab():
    return render_template('lab2.html')


@lab2.route ("/lab2/zadanie")
def zad():
    return render_template('zadanie.html')