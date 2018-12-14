from flask import Flask, request, jsonify, abort

app = Flask(__name__)


# Create some test data
users = [
	{
		'id': 0,
		'name': 'Charles',
		'age': 33,
		'occupation': 'Network Engineer'
		},
	{
		'id': 1,
		'name': 'Elvis',
		'age': 22,
		'occupation': 'Systems Developer'
		},
	{
		'id': 3,
		'name': 'Susan',
		'age': 27,
		'occupation': 'beta tester'
	}
]

@app.route("/")
def home():
	return 'function returning user list'


# A route to return all of the available users in our system
@app.route("/api/v1/users/all", methods=['GET'])
def user_all():
	return jsonify(users)

@app.route("/api/v1/users/<int:user_id>", methods=['GET'])
def user_id(user_id):

	# if 'id' in request.args:
	# 	id = int(request.args['id'])
    
	for user in users:
		if user['id'] == user_id:
			return jsonify(user)

@app.route("/api/v1/users", methods=['POST'])
def add_user():
	if not request.json or not 'name' in request.json:
		abort(404)
	else:
		
		name = request.json['name']
		age = request.json['age']
		occupation = request.json['occupation']
		user2 = {'id': 4, 'name': name, 'age': age, 'occupation': occupation}
	
	users.append(user2)
	# age = age
	# occupation = occupation
	return jsonify(users)


@app.route("/api/v1/users", methods=['PUT'])
def update_user():	

	#Check that the request string JSON format, and ID is required
	if not request.json or not 'id' in request.json:
		abort(404)
	else:

		for user in users:
			if user['id'] == request.json['id']:
				
				# id = request.json['id']
				# name = request.json['name']
				# age = request.json['age']
				# occupation = request.json['occupation'
				# user = {'id': id, 'name': name, 'age': age, 'occupation': occupation}

				return jsonify(user)
			
			# else:
			# 	return jsonify ("User not found")
						

	
		
				

if __name__ == "__main__":
	app.run(debug=True)