from flask import Flask
app = Flask (__name__)

@app.route ("/lab1")
def lab1():
    return """
<!doctype py>

<py>

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

        <footer>
            &copy; Kashirskiy Danil, FBI-14, III course, 2023
        </footer>
    </body>
</py>  
"""

@app.route ("/index")
def index():
    return """
<!doctype py>

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
                <a href="lab2" target="_blank" >Laboratory work #2</a>
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
                <a href="RGZ1" target="_blank">Control Laboratory work.</a>
            </li>  
        </ol>
    </main>

    <footer>
        &copy; Kashirskiy Danil, FBI-14, III course, 2023
    </footer>
"""