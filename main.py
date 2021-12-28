from flask import Flask,render_template,request
import os
import json

app = Flask(__name__)

@app.route('/')
def hello():
    with open('url.json', 'r', encoding = 'utf-8') as f:
        a = json.load(f)
    return render_template('index.html',a = json.dumps(a))

@app.route('/url')
def url():
    with open('url.json', 'r', encoding = 'utf-8') as f:
        a = json.load(f)
        return json.dumps(a)

app.run(debug=True)