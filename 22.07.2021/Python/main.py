from pprint import pprint
from product.Items import *
from customer.carts import *

obj = Products([{
"id": "1",
"name": "Iphone 11",
"product_details": {
"ram": "2 GB",
"processor": "snapdragon",
"screen_size": "4 inch",
},
"cost": "50000",
"currency": "INR",
"category": "mobile",
"colour": "black"
},
{
"id": "2",
"name": "Samsung Galaxy",
"product_details": {
"ram": "2 GB",
"processor": "snapdragon",
"screen_size": "4 inch",
},
"cost": "45000",
"currency": "INR",
"category": "mobile",
"colour": "grey"
},
{
"id": "3",
"name": "Washing Machine",
"product_details": {
"machine_capacity": "6kg",
"machine_rpm": "50",
"type": "top_load"
},
"cost": "25000",
"currency": "INR",
"category": "washing-machine",
"colour": "blue"
},
{
"id": "4",
"name": "Samsung TV",
"product_details": {
"isSmart": "false",
"resolution": "UHD",
"screen_size": "55 inch",
},
"cost": "40000",
"currency": "INR",
"category": "tv",
"colour": "black"
}])

cpj = carts([])
wal = Wallets()
pay = payments()

obj.display()

def addProduct():
    print("1. Mobile \n2. Washing Machine\n3. TV ")
    ch = input()
    if(ch =='1'):
        pprint(obj.add('mobiles'))
    elif(ch =='2'):
        pprint(obj.add('WashingMachines'))
    elif(ch=='3'):
        pprint(obj.add('tvs'))
    else:
        print('-------------------')

def deleteProduct():    
    id = input("Enter the id: ")
    obj.delete(id)

def admin():
    #obj.display()

    while True:
        print("1. Add Product \n2. Delete Product")
        ch = input()
        if(ch=='1'):
            addProduct()
        elif(ch=='2'):
            deleteProduct()

def payment():   
    print('1.Credit/Debit card\n2.Netbanking\n 3.Wallet\n 4.COD\n 5.Go back')
    ch=input()
    if(ch=='1'):
        pay.cardChecking() 
        customer()
    elif(ch=='2'):
        pay.netBanking()
        customer()
    elif(ch=='3'):
        pay.Wallet()
        customer()
    elif(ch=='4'):
        pay.goCod()
        customer()
    elif(ch=='5'):
        customer()
        


def viewItems(name):
    filterd = (list(filter(lambda x:x['category']==name,obj.products)))
    pprint(filterd)
    while True:
        print("1. To add item\n 2.To view Cart\n 3.To delete items from cart\n 4.Payment\n 5.Go Back")
        ch = input()
        if (ch=='1'):
            name = input("Enter the name: ") 
            for fil in filterd:
                if(fil['name']==name): 
                    cpj.toAddItem(fil)
                    print('Added Successfully')
        elif(ch=='2'):
            pprint(cpj.getItem())
        elif(ch=='3'):
            print("Enter the name of the product: ")
            ch = input()
            pprint(cpj.deleteItem(ch))
        elif(ch=='4'):
            if(len(cpj.cartItems)>=1):
                payment()
            else:
                print("Cart is Empty")
                
def customer():
     obj.display()
     while True:
        print("1. Mobile \n2. Washing Machine\n3. TV ")
        ch = input()
        if(ch =='1'):
            viewItems('mobile')
        elif(ch =='2'):
            viewItems('washing-machine')
        elif(ch=='3'):
            viewItems('tv')


while True:
    print("Who are you?")
    print("1. Admin \n2. Customer")
    ch = input()
    if(ch=='1'):
        admin()
    elif(ch=='2'):
        customer()
