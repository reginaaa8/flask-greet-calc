from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    '''returns string: "welcome"'''
    return 'welcome'

@app.route('/welcome/home')
def welcome_home():
    '''returns string: "welcome home"'''
    return 'welcome home'

@app.route('/welcome/back')
def welcome():
    '''returns string: "welcome back"'''
    return 'welcome back'

