from flask import Flask, request, Response
from flask_httpauth import HTTPBasicAuth
import pokemon_controller

app = Flask(__name__)
auth = HTTPBasicAuth()

@app.route("/pokemon", methods=["GET"])
@auth.login_required
def get_by_parameters():
    result = pokemon_controller.get_by_parameters(request.args.items())
    return Response(result, mimetype='application/json')

@auth.verify_password
def authenticate(username, password):
	if username and password:
		if username == 'admin' and password == '123':
			return True
		else:
			return False
	return False

if __name__ == "app":
    app.run(debug=True)
