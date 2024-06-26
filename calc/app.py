# Put your app in here.
from flask import Flask, request 
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def run_add():
    '''add a and b parameters'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    sum = add(a,b)
    return f"{sum}"

@app.route('/subtract')
def run_subtract():
    '''subtract a and b parameters'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    diff = sub(a,b)
    return f"{diff}"

@app.route('/multiply')
def run_multiply():
    '''multiply a and b parameters'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    product = mult(a,b)
    return f"{product}"

@app.route('/divide')
def run_divide():
    '''divide a by b parameter'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)
    return f"{result}"
