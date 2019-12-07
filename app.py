from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/jquery-3.4.1.min.js')
def jquery():
    return app.send_static_file('jquery-3.4.1.min.js')

@app.route('/script.js')
def js():
    return app.send_static_file('script.js')

@app.route('/style.css')
def style():
    return app.send_static_file('style.css')

@app.route('/logo.svg')
def logo():
    return app.send_static_file('logo.svg')

@app.route('/data')
def data():
    json_string = ''
    return Response(json_string, mimetype='application/json')