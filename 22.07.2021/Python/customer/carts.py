import datetime
import configparser
import re

config = configparser.ConfigParser()
config.read('config.ini')
print(config.sections())

class carts:    
    def __init__(self,cartItems):
        self.cartItems = cartItems

    # def viewItems(self,name):
    #     return(list(filter(lambda x:x['category']==name,products)))
    def toAddItem(self,fil):
        self.cartItems.append(fil)  
    
    def getItem(self):
        return self.cartItems
    
    def deleteItem(self,name):
        for ind,fil in enumerate(self.cartItems):
            if(fil['name']==name):
               self.cartItems.pop(ind)
        return self.getItem()


class payments:

  def cardValidate(self,number,enteredDate,cvv):
      if(not (enteredDate > datetime.datetime.today())):
          print("Card was expired")
          return False
      else:
        if(not len(number)==16):
            print("Invalid Card Number")
            return False
        if(not len(cvv)==3): 
            print("Invalid CVV")
            return False
      return True

  def cardChecking(self):
      number = input("Enter the card Number")
      date = input("Enter the Date: \n [DD-mm-yyyy]")
      dd,mm,yy =date.split('-')
      enteredDate = datetime.datetime(int(yy), int(mm), int(dd))
      cvv = input("Enter The cvv")
      
      if(input("Enter 's' to submit: ").lower()=='s'):
          if(self.cardValidate(number,enteredDate,cvv)):
              print("Transaction Success!!!")
          else:
              print("Transcaction Failed!!!")
              self.cardChecking()

  def netBanking(self):
      print("Are you sure want to Redirect?")
      ch = input("Yes/No: ").lower()
      if(ch=='yes'):
          userName = input("Enter the Username: ")
          password = input("Enter the Password: ")
          if(userName==config['NET BANKING']['username'] and password==config['NET BANKING']['password']):
              print("Transaction Success!!!")

          else:
              raise Exception("Authentication Failed!!!")

  def selectWallet(self):
        print("1.Gpay\n 2.Phonepay\n 3.Paytm")
        ch = input()
        if(ch=='1'):
            g = Gpay()
            g.setID(input('Enter the UPI ID: '))
            g.setPwd(input("Enter your password: "))
            gID = g.getID()
            if(g.validate()):
                raise Exception("Invalid UPI-ID")

            if(gID==config['GPAY']['upi id'] and g.getPwd()==config['GPAY']['pin']):
                print('Transaction Succeed!!!')
            else:
                raise Exception("Authentication Failed!!!")
        elif(ch=='2'):
            pp = PhonePay()
            pp.setID(input('Enter the UPI ID: '))
            pp.setPwd(input("Enter your password: "))
            gID = pp.getID()
            if(pp.validate()):
                raise Exception("Invalid UPI-ID")

            if(gID==config['PHONEPAY']['upi id'] and pp.getPwd()==config['PHONEPAY']['pin']):
                print('Transaction Succeed!!!')
            else:
                raise Exception("Authentication Failed!!!")
        elif(ch=='3'):
            pp = Paytm()
            pp.setID(input('Enter the UPI ID: '))
            pp.setPwd(input("Enter your password: "))
            gID = pp.getID()
            if(pp.validate()):
                raise Exception("Invalid UPI-ID")

            if(gID==config['PAYTM']['upi id'] and pp.getPwd()==config['PAYTM']['pin']):
                print('Transaction Succeed!!!')
            else:
                raise Exception("Authentication Failed!!!")


  def goCod(self):
      if(input("press 1 for place the order: ")=='1'):
          print("Order Placed!!!")
      else:
          print("Transaction Failed!!!")

class Wallets:
    _upiID = ''
    _pass=''
    
    def setID(self,ID):
        self._upiID = ID 
    
    def getID(self):
        return(self._upiID)

    def setPwd(self,pwd):
        self._pass = pwd 
    
    def getPwd(self):
        return(self._pass)

class Gpay(Wallets):
    def validate(self):
        if(re.search("@+oksi",self.getID())):
            return False
        else:
            return True

class PhonePay(Wallets):
    def validate(self):
        if(re.search("@+YPI",self.getID())):
            return False
        else:
            return True


class Paytm(Wallets):
    def validate(self):
        if(re.search("@+xyz",self.getID())):
            return False
        else:
            return True
