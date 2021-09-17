#1print(config.sections())
class Carts:
    def __init__(self,cartItems):
        self.cartItems = cartItems

    # def viewItems(self,name):
    #     return(list(filter(lambda x:x['category']==name,products)))
    def toAddItem(self,fil):
        print("app")
        self.cartItems.append(fil)

    def clearCart(self):
        self.cartItems = []

    def getItem(self):
        return self.cartItems

    def deleteItem(self,name):
        for ind,fil in enumerate(self.cartItems):
            if(fil[1]==name):
               self.cartItems.pop(ind)
        return self.getItem()
