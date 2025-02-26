from flask import Flask,render_template

myapp = Flask(__name__)

import utils

@myapp.route('/')
def home():
	return "Welcome to my Flask web app!"

if __name__ == '__main__':
	myapp.run(debug=True)