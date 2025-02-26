from flask import Flask,render_template
import utils

myapp = Flask(__name__)

@myapp.route('/')
def home():
	return "Welcome to my Flask web app!"

if __name__ == '__main__':
	myapp.run(debug=True)