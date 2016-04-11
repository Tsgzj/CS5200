import MySQLdb
import datetime

dbhandle = MySQLdb.connect("localhost","root","headbang", "ecom") #Connection to DB established
tray = dbhandle.cursor()

#1 Add/create user info
def insertuser(username, password):
    query = ("INSERT INTO User (username, password)"
            " VALUES(%s,%s)")
    args = (username, password)
    tray.execute(query, args)
    dbhandle.commit()
    return loginuser(username,password)

#1.1 login
def loginuser(username, password):
    print "Uname: %s" %username
    print "pwd: %s" %password
    query = "Select id from User where username =%s and password = %s"
    args = (username, password)
    tray.execute(query, args)
    #tray.execute("Select * from User")

    result=tray.fetchone()
    return result[0]

#1.2 Logout

#2 Get user/customer info
def getuserinfo(userid):
    try:
        #query = "Select * from User u,Customer c,Card ca, Address a ,CustomerContact cc where c.id=%s and cc.custid=c.id and a.id = c.id and ca.custid= c.id"
        query = "Select u.username from User u where u.id=%s"
        args = (userid)
        tray.execute(query, args)
    except:
        print ( "customer not found" )
    #dbhandle.commit()

    #for item in tray.fetchone():
    uname=tray.fetchone()[0]

    userinfo ={}

    if uname is not None:
        userinfo["Username"]=uname

    try:
        #query = "Select * from User u,Customer c,Card ca, Address a ,CustomerContact cc where c.id=%s and cc.custid=c.id and a.id = c.id and ca.custid= c.id"
        query = "Select * from Card where custid=%s"
        args = (userid)
        tray.execute(query, args)
    except:
        print ( "customer not found" )

    userinfo["Payment"] = []
    #print userinfo["payment"][0]

    for item in tray.fetchall():
        print item[0],item[2],item[3],item[4],item[5]
        card= {
            "CardId": item[0],
            "CardNumber":item[2],
            "Address":item[3],
            "ExpirationDate":item[4],
            "Type":item[5]
        }
        userinfo["Payment"].append(card.copy())


    try:
        #query = "Select * from User u,Customer c,Card ca, Address a ,CustomerContact cc where c.id=%s and cc.custid=c.id and a.id = c.id and ca.custid= c.id"
        query = "Select * from Address where cust_id=%s and type='billing'"
        args = (userid)
        tray.execute(query, args)
    except:
        print ( "customer not found" )

    userinfo["BillingAddress"] = []
    #print userinfo["payment"][0]

    for item in tray.fetchall():
        print item[0],item[2],item[3],item[4],item[5]
        addr= {
            "AddressId": item[0],
            "Street":item[2],
            "City":item[3],
            "State":item[4],
            "ZipCode":item[5]
        }
        userinfo["BillingAddress"].append(addr.copy())

    try:
        #query = "Select * from User u,Customer c,Card ca, Address a ,CustomerContact cc where c.id=%s and cc.custid=c.id and a.id = c.id and ca.custid= c.id"
        query = "Select * from Address where cust_id=%s and type='shipping'"
        args = (userid)
        tray.execute(query, args)
    except:
        print ( "customer not found" )

    userinfo["ShippingAddress"] = []
    #print userinfo["payment"][0]

    for item in tray.fetchall():
        print item[0],item[2],item[3],item[4],item[5]
        addr= {
            "AddressId": item[0],
            "Street":item[2],
            "City":item[3],
            "State":item[4],
            "ZipCode":item[5]
        }
        userinfo["ShippingAddress"].append(addr.copy())

    try:
        query = "select ct.id from CartOrder ct, ShoppingCart sc where sc.addedby=%s and ct.id=sc.id"
        args = (userid)
        tray.execute(query, args)
    except:
        print ( "customer not found" )

    userinfo["Order"] = []
    #print userinfo["payment"][0]

    for item in tray.fetchall():
        print item[0]
        corder= {
            "CartOrderId": item[0]
        }
        userinfo["Order"].append(addr.copy())

    return userinfo


"""

#2. Add payment info
def insertpaymentinfo(cust_id, order_id, paidwith):
    query = "INSERT INTO payment VALUES( %s%s,%s,%s,)"
    args = int(cust_id), int(order_id), int(paidwith)
    tray.execute(query, args)
    dbhandle.commit()
"""


#3. View payment info
def getpaymentnfo(custid):
    try:
        query = "Select * from Card where custid=%s"
        args = (custid)
        tray.execute(query, args)
    except:
        print ( "customer not found" )
        return None

    userinfo={}
    userinfo["Payment"] = []
    #print userinfo["payment"][0]

    for item in tray.fetchall():
        print item[0],item[2],item[3],item[4],item[5]
        card= {
            "CardId": item[0],
            "CardNumber":item[2],
            "Address":item[3],
            "ExpirationDate":item[4],
            "Type":item[5]
        }
        userinfo["Payment"].append(card.copy())

    return userinfo
"""
#4. Add cardpayment info
def insertcardpaymentinfo( cust_id, payment):
# 'cardnumber':  , 'address' : , 'expirationdate' : , 'ctype' :
    try:
        query = "Insert into card ( custid, cardnumber, address, expirationdate, type)values (%s,%s,%s,%s,%s)"
        args = int(cust_id), payment['cardnumber'], payment['address'], payment['expirationdate'], int(payment['ctype'])
        tray.execute (query, args)
    except:
        print ( "Cannot verify identity" )
    dbhandle.commit()

"""
#4. Add cardpayment info
def insertcardpaymentinfo(cust_id, cardnumber, address, expirationdate, ctype):

    expd=expirationdate.split("/")

    #print expd

    exdate=datetime.date(int(expd[2]),int(expd[1]),int(expd[0]))
    #print exdate.strftime('%Y-%m-%d')

    query = "Insert into Card (custid,cardnumber,address,expirationdate,type) values (%s,%s,%s,%s,%s)"
    args = (cust_id,cardnumber,address,exdate.strftime('%Y-%m-%d %H:%M:%S'),ctype)
    tray.execute (query,args)
    dbhandle.commit()

#5. Update Payment
def updatecardpaymentinfo(cust_id, card_id, address, expirationdate, ctype):
    expd=expirationdate.split("/")

    exdate=datetime.date(int(expd[2]),int(expd[1]),int(expd[0]))

    query = "Update Card set address = %s and expirationdate= %s and type = %s where exists (select * from Card c where c.custid = %s and c.id = %s)"
    args = (address, exdate.strftime('%Y-%m-%d %H:%M:%S'),ctype,cust_id,card_id)
    tray.execute (query, args)
    dbhandle.commit()

    #not working



#6 view inventory info
def getinventoryinfo(title):
    try:
        query = " Select * from inventory where title LIKE %s"
        args = ['%' + title + '%']
        tray.execute (query, args)
    except:
        print ("error: Cannot find inventory")
    dbhandle.commit()

    inveninfo = {}
    inveninfo["error"] = "nil"
    inveninfo["Inventory"] = []
    for item in tray.fetchall():
        print item[0],item[2],item[3],item[4],item[5]
        inven = {
            "InventoryId": item[0],
            "Discription":item[3],
            "Title":item[2],
            "Price":item[4],
            "Discount":item[5],
            "Category":item[6],
            "Available":item[7]
        }
        inveninfo["Inventory"].append(inven.copy())

    return inveninfo

    #for item in tray.fetchall():
    #print item

#7 Add an inventory
def insertinventory (title, description, price, discount, category, available,userid):
    try:
        query = " Insert into inventory(title, description, price, discount, category, available) values (%s,%s,%s,%s,%s,%s,) where exists( select * from inventorymanager i  where i.id = %s)"
        args = title, description, double(price), double (discount), int (category), int (available), int(managedby), int(userid)
        tray.execute (query, args)
    except:
        print ( " do not have permission to add" )
    dbhandle.commit()


#8. View shopping cart
def getshoppingcart(user_id):
    query = "SELECT * FROM Inventory inv, Item i WHERE exists( select *  from ShoppingCart s, Customer c, User u where inv.id = i.inv_id and i.shopcart_id = s.id and s.addedby = c.id and c.id = u.id and u.id = %s and not exists (select * from CartOrder ord where s.id=ord.id))"
    args = [user_id]
    tray.execute(query, args)
    dbhandle.commit()

    shoppingcart = {"error":"nil"}
    shoppingcart["Item"] = []
    shoppingcart["ShoppingCartId"] = ''
    for item in tray.fetchall():
        #print item[0],item[2],item[3],item[4],item[5]
        inven = {
            "InventoryId": item[0],
            "Discription":item[3],
            "Title":item[2],
            "Price":item[4],
            "Discount":item[5],
            "Category":item[6],
            "Available":item[7],
            "Quantity":item[8],
        }
        shoppingcart["Item"].append(inven.copy())
        shoppingcart["ShoppingCartId"] = item[10]

    return shoppingcart


#9. Update shopping cart
def updateshoppingcart(cartid,quant, inventory_id, user_id):
    #query = " Update item i set quantity = %s where exist (  select * from inventory in, shoppincart s , customer c, user u where i.inv_id = in.id and i.shoppingcart_id = s.id  and s.addedby = c.id  and c.id = u.id i.inv_id= %s and u.id = %s"
    query = " insert into Item(shopcart_id,inv_id,quantity) select %s,%s,%s from Inventory inv where inv.id=%s and inv.available>%s on duplicate key update quantity = if (inv.available > %s,%s,quantity)"
    args = (cartid,inventory_id,quant,inventory_id,quant,quant,quant)
    shoppingcart = {"error":"nil"}
    #int(quantity), int(inventory_id), int (user_id)
    tray.execute (query, args)
    dbhandle.commit()

    updateCartPrice(cartid)

    return shoppingcart

def updateCartPrice(cartid):
    query2="update ShoppingCart set price=(select sum(i.quantity*(inv.price-inv.discount)) from Item i, Inventory inv where i.inv_id=inv.id and shopcart_id=%s) where id=%s"
    args2=(cartid,cartid)
    tray.execute (query2, args2)
    dbhandle.commit()


#10. Delete shopping cart
def deleteshoppingcart(inventory_id, user_id,cartid):
    query = "delete from Item where inv_id=%s and shopcart_id=%s and exists (select * from User u, Customer c, ShoppingCart sc where u.id=%s and u.id=c.id and c.id=sc.addedby and sc.id=%s)"
    args =  (inventory_id,cartid,user_id,cartid)
    tray.execute (query, args)
    dbhandle.commit()
    updateCartPrice(cartid)

#11. view order detail
def getorderdetail(cartorder_id, user_id):
    query = "select co.id,inv.*,i.quantity,co.status,d.carrier,d.est_time from Inventory inv, Item i,CartOrder co,Delivery d where i.shopcart_id=%s and i.inv_id=inv.id and i.shopcart_id=co.id and co.id=d.id"
    args = [cartorder_id]

    tray.execute (query,args)
    dbhandle.commit()

    orderdetail = {"error":"nil"}
    orderdetail["Item"] = []
    orderdetail["ShoppingCartId"] = ''
    varz=tray.fetchall()
    for item in varz:
        print item[0],item[2],item[3],item[4],item[5]
        inven = {
            "InventoryId": item[1],
            "Discription":item[4],
            "Title":item[3],
            "Price":item[5],
            "Discount":item[6],
            "Category":item[7],
            "Available":item[8],
            "Quantity":item[9],
        }
        orderdetail["status"] = item[10]
        deliver = {
            "Carrier": item[11],
            "esttime": item[12]
        }
        orderdetail["Item"].append(inven.copy())
        orderdetail["Delivery"]=deliver.copy()
        orderdetail["ShoppingCartId"] = item[0]

    return orderdetail

#12. Checkout
def checkout(userid,cardid,cartid,shippingaddressid, billingaddresid):
    query = "Insert into CartOrder(id,status,shipsto) values (%s,'confirmed',%s)"
    args = (cartid,shippingaddressid)
    print query
    tray.execute (query, args)
    dbhandle.commit()
    query1 = "Insert into Payment(cust_id,order_id,paidwith) values (%s,%s,%s)"
    args1 =  (userid,cartid,cardid)
    tray.execute (query1, args1)
    dbhandle.commit()
    query2 = "Select transaction_number from Payment where order_id=%s"
    args2 =  [cartid]
    tray.execute (query2, args2)
    dbhandle.commit()
    tnumber=tray.fetchone()[0]

    checkval={}
    checkval["CartOrderId"]=cartid
    checkval["TransactionId"]=tnumber

    query3 = "Insert into ShoppingCart(addedby,price) values (%s,0)"
    args3 =  [userid]
    tray.execute (query3, args3)
    dbhandle.commit()

    return checkval


#13. Search in inventory
def search(category):
    query = " Select * from Inventory where category = %s"
    args = [category]

    #print query

    tray.execute (query,args)
    dbhandle.commit()

    invinfo={}
    invinfo["Inventory"] = []
    #print userinfo["payment"][0]

    for item in tray.fetchall():
        #print item
        #print item[0],item[2],item[3],item[4],item[5]

        invitem= {
            "InventoryId":item[0],
            "Title":item[2],
            "Description":item[3],
            "Price":item[4],
            "Discount":item[5],
            "Category":item[6],
            "Available":item[7]
        }
        invinfo["Inventory"].append(invitem.copy())


    return invinfo









"""
insertuser(username, password)
loginuser(username, password)
getuserinfo(userid)
getpaymentnfo(custid)
insertcardpaymentinfo(cust_id, cardnumber, address, expirationdate, ctype)
updatecardpaymentinfo(cardnumber, address, expirationdate, ctype, cust_id, card_id )
getinventoryinfo( title )
insertinventory (title, description, price, discount, category, available,userid)
getshoppingcart(user_id)
updateshoppingcart(quantity, inventory_id, user_id)
deleteshoppingcart(inventory_id, user_id)
getorderdetail( cartorder_id, user_id )
search(category)
"""





"""
payment = {'cardnumber': 123456789012 , 'address' : "kandivali" , 'expirationdate' : 2016-04-04 , 'ctype' : 2 }
insertcardpaymentinfo(1002, payment)
"""



"""
file = json.loads(api):
cardinfo = file.payment[cardnumber]

insertuser(username,password, cardinfo)
#insertpaymentinfo()



inquery1 = "INSERT INTO user values(123,'rty123','password')"
inquery2 = "INSERT INTO user values(124,'rty124','password')"

 #   'inquery3' : "INSERT INTO user values(125,'rty125','password')" }

#tray.execute(inquery1)
# tray.execute(inquery2)


dbhandle.commit()

tray.execute("select * from user")

for item in tray.fetchall():
    print item


"""
