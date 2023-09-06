from flask import Flask
app = Flask (__name__)

@app.route ("/")
def start():
    return """
<!doctype HTML>

<html>

    <head>
        <title>Kashirskiy Danil Sergeevich, Lab.work №1</title>
    </head>

    <body>
        <header>
            NSTU, FB, Laboratory work №1
        </header>

        <h1>WEB-server in flask</h1>

        <footer>
            &copy; Kashirskiy Danil, FBI-14, III course, 2023
        </footer>
    </body>
</html>  
"""
