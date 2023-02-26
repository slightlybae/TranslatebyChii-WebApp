from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')