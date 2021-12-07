import mysql.connector

def init():
        global mc,sql, conn
        conn  = mysql.connector.connect(host='localhost',user="root",password="water",auth_plugin='mysql_native_password')
        mc = conn.cursor(buffered=True)
        sql  = "INSERT INTO Products(name, cost, category, colour, currency) VALUES(%s, %s, %s, %s, %s)"
        mc.execute("SHOW DATABASES")
        mc.execute("USE rakeshDB")

def insert():
        val = (input("Enter the Name: "),input("Enter the cost: "),input("Enter the category: "),input("Enter the colour: "),input("Enter the currency"))
        mc.execute(sql,val)
        mc.execute("commit")

def delete():
        sql = f"DELETE FROM Products WHERE name = %s"
        val = input('Enter the Item name for Deletion: ')
        vali = (val,)
        mc.execute(sql,vali)
        mc.execute("commit")

def display():
        mc.execute("SELECT * from Products")
        for i in mc:
                print(i)

def filterd_display(name):
        fill = []
        mc.execute("SELECT * from Products")
        for i in mc:
                # print(i)
                if(i[4]==name):
                        # print(i)
                        fill.append(i)
        #print(fill)
        return fill

init()
filterd_display('mobile')
