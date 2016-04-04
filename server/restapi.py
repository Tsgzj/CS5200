#!env/bin/python
from flask import Flask, jsonify
from flask import request
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route("/session", methods=['GET'])
def login():

    app.logger.debug("JSON received...")
    #app.logger.debug(request.args)

    if not request.args or not request.args.get('username') or not request.args.get('password'):
        abort(400)

    if request.args:
        #mydata = request.json
        username = request.args.get('username')
        password = request.args.get('password')

        #TODO: return user id

        user_id = {
        	"error":"nil",
        	"uid":123
        }

        if (user_id is None):
	        user_id = {
	        	"error":"Can not verify username/password"
	        }
	        return jsonify(user_id),401

        return jsonify(user_id),200

    else:
        return "no json received"

@app.route("/session", methods=['DELETE'])
def logout():

    app.logger.debug("JSON received...")
    app.logger.debug(request.json)

    if not request.json:
        abort(400)

    if request.json:
        mydata = request.json

        #TODO: return user id

        resp = {"error":"Bad logout"}

        if mydata.get("uid") == -1:
        	resp = {"error":"nil"}
        	return jsonify(resp),200

        return jsonify(resp),401
    else:
        return "no json received"

@app.route("/user", methods=['GET'])
def getuserinfo():

    app.logger.debug("JSON received...")
    app.logger.debug(request.json)

    if not request.json:
        abort(400)

    if request.json:
        mydata = request.json

        uid = mydata.get("uid")

        #TODO : Get details from uid
        resp = {"stub":"get uid details"}

        if (resp is None):
	        resp = {
	        	"error":"Cannot find user info"
	        }
	        return jsonify(resp),401

        return jsonify(resp),200
    else:
        return "no json received"

@app.route("/user/payment", methods=['GET'])
def getcards():

    app.logger.debug("JSON received...")
    app.logger.debug(request.json)

    if not request.json:
        abort(400)

    if request.json:
        mydata = request.json

        uid = mydata.get("uid")

        #TODO : Get details from uid to return list of cards
        resp = {"stub":"get uid details"}

        if (resp is None):
	        resp = {
	        	"error":"No Card info"
	        }
	        return jsonify(resp),401

        return jsonify(resp),200
    else:
        return "no json received"





if __name__ == '__main__':
    app.run(debug=True)
