from flask import Flask
from flask import request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def indexPage():
    return render_template('landing.html')


if __name__ == '__main__':
    app.run()