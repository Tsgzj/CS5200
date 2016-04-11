#!env/bin/python
from __future__ import print_function # In python 2.7
from flask import Flask, jsonify
from flask import request
from flask import abort
from dbword import *
import time
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route("/session")
def login():

    username = request.args.get('username')
    password = request.args.get('password')

    uid=loginuser(username,password)

    if (uid is None):
        user_id = {
            "error":"Can not verify username/password"
        }
        return jsonify(user_id),401

    user_id = {
    	"error":"nil",
    	"UserId":uid
    }

    return jsonify(user_id),200

@app.route("/session/add")
def adduser():

    username = request.args.get('username')
    password = request.args.get('password')

    #TODO: return user id
    uid=insertuser(username,password)

    if (uid is None):
        user_id = {
            "error":"Can not add new username/password"
        }
        return jsonify(user_id),401

    user_id = {
        "error":"nil",
        "UserId":uid
    }

    return jsonify(user_id),200


@app.route("/session", methods=['DELETE'])
def logout():

    app.logger.debug("JSON received...")
    app.logger.debug(request.json)

    if not request.json:
        abort(400)

    if request.json:
        mydata = request.json

        resp = {"error":"nil"}
        return jsonify(resp),200

@app.route("/user", methods=['GET'])
def retrieveuserinfo():

    uid = request.args.get('UserId')

    #TODO : Get details from uid
    resp = getuserinfo(uid)

    if (resp is None):
        resp = {"error":"Cannot find user info"}
        return jsonify(resp),401

    #resp['error'] = 'nil'

    return jsonify(resp),200

@app.route("/user/payment", methods=['GET'])
def getcards():

    uid = request.args.get('UserId')

    #TODO : Get details from uid to return list of cards
    resp = getpaymentnfo(uid)

    if (resp is None):
        resp = {
        	"error":"UserId not found"
        }
        return jsonify(resp),401

    return jsonify(resp),200

@app.route("/user/updatepayment",methods=['POST'])
def updatecard():

    cardid = request.args.get('cardId')

    if not request.json:
        abort(400)

    if request.json:
        req=request.json

        uid=req.get("UserId")
        cardnum=req.get("CardNumber")
        address=req.get("Address")
        expdate=req.get("ExpirationDate")
        ctype=req.get("Type")

        updatecardpaymentinfo(uid,cardid,cardnum,address, expdate, ctype)

        resp = {"error":"nil"}

        return jsonify(resp),200

@app.route("/user/payment",methods=['POST'])
def addcard():

    if not request.json:
        abort(400)

    if request.json:

        req=request.json

        uid=req.get("UserId")
        cardnum=req.get("CardNumber")
        address=req.get("Address")
        expdate=req.get("ExpirationDate")
        ctype=req.get("Type")

        insertcardpaymentinfo(uid,cardnum,address,expdate,ctype)

        resp = {"error":"nil"}

        return jsonify(resp),200



@app.route("/inventory",methods=['GET'])
def getinventory():

    invname = request.args.get('title')

    resp = getinventoryinfo(invname)
    print("RESP::::::%s" % resp)

    return jsonify(resp),200

@app.route("/inventory",methods=['POST'])
def addinventory():

    if not request.json:
        abort(400)

    if request.json:
        req=request.json

        uid=req.get("UserId")
        title=req.get("Title")
        descp=req.get("Description")
        price=req.get("Price")
        discount=req.get("Discount")
        category=req.get("Category")
        available=req.get("Available")

    resp = insertinventory (title, descp, price, discount, category, available,uid)

    return jsonify(resp),200

@app.route("/shoppingcart",methods=['GET'])
def getcart():

    uid = request.args.get('UserId')

    #getshoppingcartdetails
    resp = getshoppingcart(uid)

    if(resp is None):
        resp = {"error":"Cannot verify identity"}
        return jsonify(resp),401

    return jsonify(resp),200

@app.route("/shoppingcart",methods=['POST'])
def updatecart():

    if not request.json:
        abort(400)

    if request.json:
        req=request.json

        uid=req.get("UserId")
        cartid=req.get("ShoppingCartId")
        quant=req.get("Quantity")
        invid=req.get("InventoryId")

    #add/update shopping cart

        resp = updateshoppingcart(cartid,quant,invid,uid)

    return jsonify(resp),200

@app.route("/shoppingcart",methods=['DELETE'])
def removefromcart():

    uid = request.args.get('userid')
    inventoryid = request.args.get('inventoryid')
    shoppingcartid = request.args.get('shoppingcartid')

    resp = deleteshoppingcart(inventoryid,uid,shoppingcartid)


    #remove from cart

    resp =  {"error":"nil"}

    return jsonify(resp),200

@app.route("/order",methods=['GET'])
def getorder():

    uid = request.args.get('UserId')
    CartOrderID = request.args.get('CartOrderId')

    resp = getorderdetail(CartOrderID,uid)

    return jsonify(resp),200

@app.route("/order",methods=['POST'])
def createorder():

    if not request.json:
        abort(400)

    if request.json:
        req=request.json

        uid=req.get("UserId")
        cardid=req.get("CardId")
        cartid=req.get("CartId")
        saddress=req.get("ShippingAddressId")
        baddress=req.get("BillingAddressId")

        resp=checkout(uid,cardid,cartid,saddress,baddress)

        resp ["error"]="nil"

    return jsonify(resp),200

@app.route("/category",methods=['GET'])
def getcategory():

    cate = request.args.get('category')

    #list all items from a category

    resp=search(cate)

    resp ["error"]="nil"

    return jsonify(resp),200








if __name__ == '__main__':
    app.run(debug=True)
