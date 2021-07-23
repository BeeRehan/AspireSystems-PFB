from product.Items import *

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