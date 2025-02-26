from flask import jsonify, request
from app import myapp  # Import the myapp instance

@myapp.route('/greet_user', methods=['GET'])
def greet_user():
	"""
	Endpoint to greet a user.
	Example usage: /greet_user?name=Michael
	"""
	name = request.args.get('name', 'Guest')
	message = f"Hello, {name}!"
	return jsonify({'message': message})