from pprint import pprint
from db import database
from customer.carts import *
from customer.payments import *
#
database.init()
database.display()
cpj = Carts([])

def payment():
    print('1.Credit/Debit card\n2.Netbanking\n 3.Wallet\n 4.COD\n 5.Go back')
    ch=input()
    if(ch=='1'):
        cd = CardPayement()
        cd.initiate()
        cpj.clearCart()
        customer()
    elif(ch=='2'):
        nb = NetBanking()
        nb.initiate()
        cpj.clearCart()
        customer()
    elif(ch=='3'):
        print("Choose your Wallet")
        ch = input("1.GPAY\n2.PHONEPAY\n3.PAYTM\n")
        if(ch=='1'):
            ch = 'GPAY'
        elif(ch=='2'):
            ch = 'PHONEPAY'
        elif(ch=='3'):
            ch = 'PAYTM'

        wt = Wallets(ch)
        wt.initiate()
        cpj.clearCart()
        customer()
    elif(ch=='4'):
        cod = Cod()
        cod.initiate()
        cpj.clearCart()
        customer()
    elif(ch=='5'):
        customer()

def admin():
    while True:
        print("What do you want???")
        ch = input("1.Add Data\n2.View data\n3.Delete data")
        if(ch=='1'):
            database.insert()
        elif(ch=='2'):
            database.display()
        elif(ch=='3'):
            database.delete()
        else:
            print('-----------------')

def formatDisplay(filterd):
    for filll in filterd:
        print(f"Name: {filll[1].capitalize() }\nPrice: {filll[2].capitalize() } {filll[3].capitalize() }\nCategory: {filll[4].capitalize() }\nColor: {filll[5].capitalize() }\n")

def viewItems(name):
    filtered = database.filterd_display(name)
    formatDisplay(filtered)
    while True:
        print("1. To add item\n 2.To view Cart\n 3.To delete items from cart\n 4.Payment\n 5.Go Back")
        ch = input()
        if (ch=='1'):
            name = input("Enter the name: ")
            for fil in filtered:
                print(print(fil[1])==name)
                if(fil[1]==name):
                    print("card")
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
     database.display()
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
        if(input("Enter the passcode: ")=="admin"):
            admin()
        else:
            raise Exception("Authentication Failed!!!")
    elif(ch=='2'):
        customer()
