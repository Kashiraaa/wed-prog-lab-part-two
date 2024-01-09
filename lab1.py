from flask import Blueprint, redirect, url_for, render_template
lab1 = Blueprint ('lab1', __name__)

@lab1.route ("/lab1")
def lab():
    return """
<!doctype html>

<html>

    <head>
        <title>Kashirskiy Danil Sergeevich, Lab.work №1</title>
    </head>

    <body>

        <header>
            NSTU, FB, Laboratory work №1
        </header>

        <h1>WEB-server in flask</h1>

        <p>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug,  также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности. 
        </p>

        <li><a href="menu" target="_blank" >Laboratory menu</a></li>

        <footer>
            &copy; Kashirskiy Danil, FBI-14, III course, 2023
        </footer>

    </body>
</html>  
"""


@lab1.route ("/index")
def index():
    return redirect("/menu", code=302)


@lab1.route ("/menu")
def menu():
    return """
<!doctype html>

<html>
    <head>
        <title>Kashirskiy Danil Sergeevich, Lab.work lobby</title>
    </head>

    <main>
        <h1>Laboratory works, WEB-programming</h1>
        
        <ol>
            <li>
                <a href="lab1" target="_blank" >Laboratory work #1</a>
            </li>
            <li>
                <a href="lab1/lab1pic" target="_blank">Laboratory work #1(good tree)</a>
            </li>
            <li>
                <a href="lab1/student" target="_blank">Laboratory work #1(student)</a>
            </li>
            <li>
                <a href="lab1/pythome" target="_blank">Laboratory work #1(python)</a>
            </li>
            <li>
                <a href="lab1/yamaguchi" target="_blank">Laboratory work #1(Yamaguchi)</a>
            </li>
            <li>
                <a href="lab2/" target="_blank" >Laboratory work #2</a>
            </li>
            <li>
                <a href="lab3" target="_blank">Laboratory work #3</a>
            </li>
            <li>
                <a href="lab4" target="_blank">Laboratory work #4</a>
            </li>
            <li>
                <a href="lab5" target="_blank">Laboratory work #5</a>
            </li>
            <li>
                <a href="lab6" target="_blank">Laboratory work #6</a>
            </li>
            <li>
                <a href="lab7" target="_blank">Laboratory work #7</a>
            </li>
            <li>
                <a href="lab8" target="_blank">Laboratory work #8</a>
            </li>
            <li>
                <a href="lab9" target="_blank">Laboratory work #9</a>
            </li>
            <li>
                <a href="RGZ1" target="_blank">Control Laboratory work.</a>
            </li>  
        </ol>
    </main>

    <footer>
        &copy; Kashirskiy Danil, FBI-14, III course, 2023
    </footer>
</html>
"""


@lab1.route ("/lab1/lab1pic")
def lab1pic():
    return '''
<!doctype html>

<html>

    <head>
        <title>Kashirskiy Danil Sergeevich, Lab.work №1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>

    <body>

        <header>
            NSTU, FB, Laboratory work №1
        </header>

        <h1>Хорошее дерево</h1>

        <img src="''' + url_for('static', filename='lab1pic.jpg') + '''" style="margin: 10px auto 20px; display: block;">
        
        <footer>
            &copy; Kashirskiy Danil, FBI-14, III course, 2023
        </footer>

    </body>
</html>  
'''


@lab1.route ("/lab1/student")
def lab1student():
    return '''
<!doctype html>

<html>

    <head>
        <title>Kashirskiy Danil Sergeevich, Lab.work №1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>

    <body>

        <header>
            NSTU, FB, Laboratory work №1
        </header>

        <h1>Kashirskiy Danil Sergeevich</h1>

        <img src="''' + url_for('static', filename='lab1nstu.jpg') + '''" style="margin: 10px auto 20px; display: block; width: 45%">
        
        <footer>
            &copy; Kashirskiy Danil, FBI-14, III course, 2023
        </footer>

    </body>
</html>  
'''


@lab1.route ("/lab1/pythome")
def pythome():
    return '''
<!doctype html>

<html>

    <head>
        <title>Kashirskiy Danil Sergeevich, Lab.work №1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>

    <body>

        <header>
            NSTU, FB, Laboratory work №1
        </header>

        <h1>Что такое Python ?</h1>

        <p>
        Python — это язык программирования, который широко используется в интернет-приложениях, 
        разработке программного обеспечения, науке о данных и машинном обучении (ML). 
        Разработчики используют Python, потому что он эффективен, 
        прост в изучении и работает на разных платформах. Программы на языке Python можно скачать бесплатно, 
        они совместимы со всеми типами систем и повышают скорость разработки.
        </p>

        <img src="''' + url_for('static', filename='piton.png') + '''" style="margin: 10px auto 20px; display: block; width: 20%">

        <h2>Где применяется Python ?</h2>

        <p>
        Веб-разработка на стороне сервера включает в себя сложные серверные функции, 
        с помощью которых веб-сайты отображают информацию для пользователя. 
        Например, веб-сайты должны взаимодействовать с базами данных и другими веб-сайтами, а также защищать данные при их отправке по сети. 

        Python полезен при написании серверного кода, поскольку он предлагает множество библиотек, 
        состоящих из предварительно написанного кода для сложных серверных функций. 
        Также разработчики используют широкий спектр платформ Python, 
        которые предоставляют все необходимые инструменты для более быстрого и простого создания интернет-приложений. 
        Например, разработчики могут создать «скелет» интернет-приложения за считанные секунды, потому что им не нужно писать код с нуля. 
        Затем его можно протестировать с помощью инструментов тестирования платформы независимо от внешних инструментов тестирования.
        </p>


        <footer>
            &copy; Kashirskiy Danil, FBI-14, III course, 2023
        </footer>

    </body>
</html>  
'''


@lab1.route ("/lab1/yamaguchi")
def yamaguchi():
    return '''
<!doctype html>

<html>

    <head>
        <title>Kashirskiy Danil Sergeevich, Lab.work №1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>

    <body>

        <header>
            NSTU, FB, Laboratory work №1
        </header>

        <h1>Современное японское оборудование от Yamaguchi</h1>

        <p>
        YAMAGUCHI — одна из лидирующих компаний в мире, которая задаёт тренды в области массажного оборудования, 
        фитнес-тренажеров, товаров для красоты и здоровья! Мы являемся официальными дистрибьюторами известных мировых производителей, 
        среди которых Yamaguchi, US Medica, Fujiiryoki, Hakuju, Bestec и Anatomico.
        
        Миссия компании Yamaguchi — прививать любовь к здоровью! 
        Мы заботимся о качестве жизней наших клиентов, разрабатывая продукцию по последним 
        техническим и дизайнерским новшествам совместно с врачами-мануальными терапевтами, 
        врачами-косметологами и профессиональными фитнес-тренерами. 
        Каждая новинка перед выходом проходит строгий контроль качества и многократно тестируется, что подтверждает 
        безопасность и надежность. Наше оборудование позволяет 
        моментально восстановить энергию и силы, привести фигуру в форму, 
        поддержать идеальный вес, укрепить здоровье и позаботиться о красоте. В совокупности 
        со стильным дизайном и передовыми японскими технологиями каждый продукт — настоящий шедевр!
        </p>

        <img src="''' + url_for('static', filename='kreslo.jpg') + '''" style="margin: 10px auto 20px; display: block; width: 45%">

        <p>
        Наша компания объединяет Россию здоровьем! В салонах Yamaguchi от Калининграда до Владивостока можно познакомиться с брендом, 
        протестировать продукцию и получить профессиональную консультацию от менеджеров. 
        Доставку мы осуществляем через собственную логистическую службу в течение 24-х часов по всей России. 
        Сотрудники логистики — профессионалы, которые не только доставляют оборудование в нужное помещение, 
        но и подробно рассказывают о товаре и обучают им пользоваться.
        </p>


        <footer>
            &copy; Kashirskiy Danil, FBI-14, III course, 2023
        </footer>

    </body>
</html>  
'''
