import MySQLdb

dbhandle = MySQLdb.connect("localhost","root","headbang", "ecom") #Connection to DB established
tray = dbhandle.cursor()

#1 Add/create user info
def insertuser(username, password):
    query = ("INSERT INTO User (username, password)"
            " VALUES(%s,%s)")
    args = (username, password)
    tray.execute(query, args)
    dbhandle.commit()
    
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
        query = "Select * from User u,Customer c,Card ca, Address a ,CustomerContact cc where  %s=c.id and cc.custid=c.id and a.id = c.id and ca.custid= c.id"
        args = userid
        tray.execute(query, args)
    except:
        print ( "customer not found" )
    dbhandle.commit()
    return tray.fetchall()
    #for item in tray.fetchall():
    #print item
        

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
    query = " Select * from card ca where ca.custid = %s"  
    args = int(custid)
    tray.execute ( query, args)
    dbhandle.commit()
    return tray.fetchall()
    #for item in tray.fetchall():
    #print item
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
    try:
        query = "Insert into card ( custid, cardnumber, address, expirationdate, type)values (%s,%s,%s,%s,%s)"
        args = int(cust_id), cardnumber, address, expirationdate, int(ctype)
        tray.execute (query, args) 
    except:
        print ( "Cannot verify identity" )
    dbhandle.commit()



#5. Update Payment
def updatecardpaymentinfo(cardnumber, address, expirationdate, ctype, cust_id, card_id ):
    try:
        query = "Update card set cardnumber = %s and address = %s and expirationdate= %s and type = %s where exists ( select * from card where card.custid = %s and card.id = %s)"
        args = cardnumber, address, expirationdate ,int(ctype), int(cust_id), int(card_id)
        tray.execute (query, args)
    except:
        print ( "Cannot verify identity" )
    dbhandle.commit()


        
#6 view inventory info 
def getinventoryinfo( title ):
    try:
        query = " Select * from inventory where title = %s"
        args = title 
        tray.execute (query, args)
    except:
        print ("error: Cannot find inventory")
    dbhandle.commit()
    return tray.fetchall()
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
    try:
        query = " Select * from inventory in where exists ( select * item i, shoppincart s , customer c, user u where i.inv_id = in.id and i.shoppingcart_id = s.id  and s.addedby = c.id  and c.id = u.id and u.id = %s"
        args = int (user_id)
        tray.execute (query, args)
    except:
        print ( " cannot verify identity" )
    dbhandle.commit() 


                       
#9. Update shopping cart
def updateshoppingcart(quantity, inventory_id, user_id):
    try:
        query = " Update item i set quantity = %s where exist (  select * from inventory in, shoppincart s , customer c, user u where i.inv_id = in.id and i.shoppingcart_id = s.id  and s.addedby = c.id  and c.id = u.id i.inv_id= %s and u.id = %s"
        args = int(quantity), int(inventory_id), int (user_id)
        tray.execute (query, args)
    except:
        print ( " cannot verify identity" )
    dbhandle.commit() 
    

#10. Delete shopping cart
def deleteshoppingcart(inventory_id, user_id):
    try:
        query = " delete from item i where exist (  select * from inventory in, shoppincart s , customer c, user u where i.inv_id = in.id and i.shoppingcart_id = s.id  and s.addedby = c.id  and c.id = u.id and i.inv_id= %s and u.id = %s"
        args =  int(inventory_id), int (user_id)
        tray.execute (query, args)
    except:
        print ( "cannot verify identity" )
    dbhandle.commit()
    
#11. view order detail
def getorderdetail( cartorder_id, user_id ):
    try:
        query = " select  * from item where exist (  select * from  shoppingcart s, cartoder co, inventory in, customer c, user u where in.id= i.inv_id and i.shoppingcart_id = s.id  and s.addedby = c.id  and c.id = u.id and co.id = s.id and co.id = %s and u.id = %s"
        args =  int(cartorder_id), int (user_id)
        tray.execute (query, args)
    except:
        print ( "cannot verify identity" )
    dbhandle.commit()
    
#12. Checkout
"""
def checkout(userid):
    try:
        query: "
"""

#13. Search in inventory
def search(category):
    try:
        query = " Select * from inventory where category = %s"
        args = int(category) 
        tray.execute (query, args)
    except:
        print ("error: Cannot find the category")
    dbhandle.commit()
    return tray.fetchall()
    #for item in tray.fetchall():
    #print item









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



