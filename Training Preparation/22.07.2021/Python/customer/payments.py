import datetime
import re
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


class Payments:

  types = {
      'CARD' : ['number','pin','cvv','date','otp'],
      'NET BANKING' :['username','password'],
       'Wallet' :  ['upi id','pin'],
       'COD':['pwd']
    #    dt:{
    #        nu : {int
    #    }
  }

  def get_input(self,Class):
      inDic = dict()

      for key in self.types[Class]:
          inDic[key] = input("Enter the {0}: ".format(key))
      return inDic

  def validate(self,inDic,Class):
      flag =  True

      for key in inDic.keys():
          #print(inDic[key])
          if(not (inDic[key] == config[Class][key])):
              flag = False
      if(flag):
          print("Order Successful!!!")
      else:
          raise Exception("Authentication Failed!!!")


class CardPayement(Payments):

    # Class  = 'CARD'
    credential = ''

    def __init__(self):
        self.credential = self.get_input('CARD')

    def reg_check(self,credential):
        enterDate = credential['date']
        dd,mm,yy = enterDate.split('-')
        enterDate = datetime.datetime(int(yy), int(mm), int(dd))
        if(not (enterDate > datetime.datetime.today())):
          print("Card was expired")
          return False
        else:
           # print(len(credential['number']))
            if(not len(credential['number'])==19):
                print("Invalid Card Number")
                return False
            if(not len(credential['cvv'])==3):
                print("Invalid CVV")
                return False
        return True

    def initiate(self):
        if(self.reg_check(self.credential)):
            self.validate(self.credential,'CARD')

class NetBanking(Payments):
    # Class = 'NET BANKING'
    credential = ''
    def initiate(self):
        print("Are you sure want to Redirect?")
        ch = input("Yes/No: ").lower()
        if(ch=='yes'):
            self.credential = self.get_input('NET BANKING')
            self.validate(self.credential,'NET BANKING')

class Wallets(Payments):
    # Class = 'Wallet'
    credential = ''
    ind = 0
    Wallet = {'GPAY':'oksi',
            'PHONEPAY':'YPI',
            'PAYTM':'oksi'
    }

    def __init__(self,ind):
        self.ind = ind
        self.credential = self.get_input('Wallet')

    def reg_validate(self):
        if(re.search("@+{0}".format(self.Wallet[self.ind]),self.credential['upi id'])):
            return True
        else:
            return False
    def initiate(self):
        if(self.reg_validate):
            self.validate(self.credential,self.ind)

class Cod(Payments):

    def initiate(self):
        if(input("Are you want to place the order?\nYes/No: ")):
            self.validate(self.get_input('COD'),"COD")

# class Sample:
#     def __init__(MD,name):
#         MD.name  = name

#     def dis(MD):
#         print(MD.name)

# S = Sample("yasin")
# S.dis()
#
# class Gpay('Wallets'):
#     pass


# class Phonepay('Wallets'):
#     pass

# class Paytm('Wallets'):
#     pass
#
#   def cardValidate(self,number,enteredDate,cvv):
#       if(not (enteredDate > datetime.datetime.today())):
#           print("Card was expired")
#           return False
#       else:
#         if(not len(number)==16):
#             print("Invalid Card Number")
#             return False
#         if(not len(cvv)==3):
#             print("Invalid CVV")
#             return False
#       return True

#   def cardChecking(self):
#       number = input("Enter the card Number")
#       date = input("Enter the Date: \n [DD-mm-yyyy]")
#       dd,mm,yy =date.split('-')
#       enteredDate = datetime.datetime(int(yy), int(mm), int(dd))
#       cvv = input("Enter The cvv")

#       if(input("Enter 's' to submit: ").lower()=='s'):
#           if(self.cardValidate(number,enteredDate,cvv)):
#               print("Transaction Success!!!")
#           else:
#               print("Transcaction Failed!!!")
#               self.cardChecking()

#   def netBanking(self):
#       print("Are you sure want to Redirect?")
#       ch = input("Yes/No: ").lower()
#       if(ch=='yes'):
#           userName = input("Enter the Username: ")
#           password = input("Enter the Password: ")
#           if(userName==config['NET BANKING']['username'] and password==config['NET BANKING']['password']):
#               print("Transaction Success!!!")

#           else:
#               raise Exception("Authentication Failed!!!")

#   def selectWallet(self):
#         print("1.Gpay\n 2.Phonepay\n 3.Paytm")
#         ch = input()
#         if(ch=='1'):
#             g = Gpay()
#             g.setID(input('Enter the UPI ID: '))
#             g.setPwd(input("Enter your password: "))
#             gID = g.getID()
#             if(g.validate()):
#                 raise Exception("Invalid UPI-ID")

#             if(gID==config['GPAY']['upi id'] and g.getPwd()==config['GPAY']['pin']):
#                 print('Transaction Succeed!!!')
#             else:
#                 raise Exception("Authentication Failed!!!")
#         elif(ch=='2'):
#             pp = PhonePay()
#             pp.setID(input('Enter the UPI ID: '))
#             pp.setPwd(input("Enter your password: "))
#             gID = pp.getID()
#             if(pp.validate()):
#                 raise Exception("Invalid UPI-ID")

#             if(gID==config['PHONEPAY']['upi id'] and pp.getPwd()==config['PHONEPAY']['pin']):
#                 print('Transaction Succeed!!!')
#             else:
#                 raise Exception("Authentication Failed!!!")
#         elif(ch=='3'):
#             pp = Paytm()
#             pp.setID(input('Enter the UPI ID: '))
#             pp.setPwd(input("Enter your password: "))
#             gID = pp.getID()
#             if(pp.validate()):
#                 raise Exception("Invalid UPI-ID")

#             if(gID==config['PAYTM']['upi id'] and pp.getPwd()==config['PAYTM']['pin']):
#                 print('Transaction Succeed!!!')
#             else:
#                 raise Exception("Authentication Failed!!!")


#   def goCod(self):
#       if(input("press 1 for place the order: ")=='1'):
#           print("Order Placed!!!")
#       else:
#           print("Transaction Failed!!!")

# class Wallets:
#     _upiID = ''
#     _pass=''

#     def setID(self,ID):
#         self._upiID = ID

#     def getID(self):
#         return(self._upiID)

#     def setPwd(self,pwd):
#         self._pass = pwd

#     def getPwd(self):
#         return(self._pass)

# class Gpay(Wallets):
#     def validate(self):
#         if(re.search("@+oksi",self.getID())):
#             return False
#         else:
#             return True

# class PhonePay(Wallets):
#     def validate(self):
#         if(re.search("@+YPI",self.getID())):
#             return False
#         else:
#             return True


# class Paytm(Wallets):
#     def validate(self):
#         if(re.search("@+xyz",self.getID())):
#             return False
#         else:
#             return True
