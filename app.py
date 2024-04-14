import json
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    fileData = open(file="./data/data.json", mode="r", encoding='utf-8')
    data = fileData.read()
    fileData.close()
    response = render_template(
        'index.html',
        name=name,
        items=json.loads(data)
    )
    return response
