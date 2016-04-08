import MySQLdb

#1 Add/create user info
def insertuser(username, password):
    try:
        #userid = raw_input("enter user id")
        #name = raw_input("enter user name")
        #password = raw_input("enter user password")
        #query= "Delete from user"
        query = "INSERT INTO user (username, password) VALUES(%s,%s)"
        args = name, password
        tray.execute(query, args)
    except:
        print ("check for data type or foreign key error")
        dbhandle.commit()

#2 Get user/customer info
def getuserinfo(userid):
    try:
        query = "Select * from User u,Customer c,Card ca, Address a ,CustomerContact cc where  %s=c.id and cc.custid=c.id and a.id = c.id and ca.custid= c.id"
        args = userid
        tray.execute(query, args)
    except:
        print ( "customer not found" )
        dbhandle.commit()
    for item in tray.fetchall():
    return item
        



#2. Add payment info
def insertpaymentinfo(cust_id, order_id, paidwith):
    query = "INSERT INTO payment VALUES( %s%s,%s,%s,)"
    args = int(cust_id), int(order_id), int(paidwith)
    tray.execute(query, args)
    dbhandle.commit()
    
#3. View payment info 
def getpaymentnfo(custid)
    query = " Select * from card ca where ca.custid = %s"  
    args = int(custid)
    tray.execute ( query, args)
    dbhandle.commit()
    for item in tray.fetchall():
    return item

#4. Add cardpayment info
def insertcardpaymentinfo( cust_id, cardnumber, address, expirationdate, ctype )
    query = "Insert into card ( custid, cardnumber, address, expirationdate, type)values (%s,%s,%s,%s,%s)"
    args = int(cust_id), cardnumber, address, expirationdate ,int(ctype)
    tray.execute (query, args)
    dbhandle.commit()

#5 view inventory info 
def getinventoryinfo(invent_id)
try:
    query = " Select * from inventory where id = %s"
    args = int(invent_id)
    tray.execute (query, args)
except:
    print ("error: Cannot find inventory")
    dbhandle.commit()
    for item in tray.fetchall():
    return item

#6 Add an inventory
def insertinventory (managedby, title, description, price, discount, category, available)
    query = " Insert into inventory( managedby, title, description, price, discount, category, available) values (%s,%s,%s,%s,%s,%s,%s) 
    args = int(managedby), title, description, double(price), double (discount), int (category), int (available)
    tray.execute (query, args)
    dbhandle.commit()

#7 
                           
    







"""













    

dbhandle = MySQLdb.connect("localhost","root","toor", "ecom") #Connection to DB established
tray = dbhandle.cursor()


insertuser()
#insertpaymentinfo()

"""
inquery1 = "INSERT INTO user values(123,'rty123','password')"
inquery2 = "INSERT INTO user values(124,'rty124','password')"

 #   'inquery3' : "INSERT INTO user values(125,'rty125','password')" }

#tray.execute(inquery1)
# tray.execute(inquery2)
"""

dbhandle.commit()

tray.execute("select * from user")

for item in tray.fetchall():
    print item






