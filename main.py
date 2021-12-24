from flask import Flask,render_template
import os

app = Flask(__name__)

@app.route('/')
def hello():
    a = os.listdir(r'doc')
    return render_template('index.html',a = a)

app.run(debug=True)