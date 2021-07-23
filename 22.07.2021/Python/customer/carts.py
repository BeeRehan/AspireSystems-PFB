from product.Items import *
import datetime

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
      ch = input("Yes/No").lower()
      if(ch=='yes'):
          userName = input("Enter the Username")
          password = input("Enter the Password")
          if(userName=='' and password==''):
              print("Transaction Success!!!")

      else:
          print("Transcaction Failed!!!")

  def Wallet(self):
      print("Wallet transaction not available!!!")

  def goCod(self):
      if(input("press 1 for place the order: ")=='1'):
          print("Order Placed!!!")
      else:
          print("Transaction Failed!!!")

class Wallets:
    _upiID = ''
    
    def setID(self,ID):
        self._upiID = ID 
    
    def getID(self):
        return(self._upiID)
    