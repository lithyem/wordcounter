from flask import Flask,render_template
myapp = Flask(__name__)

@myapp.route('/')
def home():
	return "Welcome to my Flask web app!"