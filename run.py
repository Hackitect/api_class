from flask import Flask, request, jsonify

app = Flask(__name__)


# Create some test data
users = [
	{
		'name': 'Charles',
		'age': 33,
		'occupation': 'Network Engineer'
		},
	{
		'name': 'Elvis',
		'age': 22,
		'occupation': 'Systems Developer'
		},
	{
		'name': 'Susan',
		'age': 27,
		'occupation': 'beta tester'
	}
]

@app.route("/")
def home():
	return '''<h1>User list API</h1>
<p>A prototype API for returning user object with age and occupation.</p>'''


# A route to return all of the available users in our system
@app.route("/users", methods=['GET'])
def api_all():
	return jsonify(users)



@app.route("/users/name", methods=['GET'])
def get_user(name):

	results = []
	for user in users:
		if user['name'] == user:
			results.append(user)
			return jsonify(user), 200
		else:
			return 'User not found in system', 404

@app.route("/users/name", methods=['POST'])
def add_user(self, name):
	for user in users:
		if (name == user['name']):
			return user, 200
		return 'User not found in system', 404



if __name__ == "__main__":
	app.run(debug=True)