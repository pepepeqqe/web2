from flask import Flask
app = Flask (__name__)

@app.route("/")
def start():
    return """
            <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Гунгер Кирилл Андреевич, Лабораторная 1</title>
        </head>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>
            <h1>web-сервер на flask</h1>
            <footer>
                &copy; Гунгер Кирилл, ФБИ-23, 3 курс, 2025
            </footer>
        </body>
    </html>
    """
