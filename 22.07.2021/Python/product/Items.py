class Products:

    crendials = {
      'commons':['id','name','cost','currency','category','colour'],
      'mobiles' : ['ram','processor','screen_size'],
      'WashingMachines' : ['machine_capacity','machine_rpm','type'],
      'tvs' : ['isSmart','resolution','screen_size'],
    }

    def __init__(self,products):
        self.products = products
    
    def display(self):
        #return(self.products)
        for product in self.products:
            print(f"Name:{product['name']}\nCost:{product['cost']} {product['currency']}\nCategory:{product['category']}\n")
        
    def add(self,ind):
        #print("Arrived")
        self.products.append(self.getInput(ind))
        return(self.products)

    def getInput(self,ip):
        inp = dict()
        inner = dict()
        print(ip)
        for common in self.crendials['commons']:
          inp[common] = input("Enter the {0}".format(common)) 
        
        for cat in self.crendials[ip]:
          inner[cat] = input("Enter {0}".format(cat))
        
        inp.update({"product_details":inner})
        
        return(inp)

    def delete(self,id):
        for index,product in enumerate(self.products):
          if(product['id']==id):
            self.products.pop(index)
        self.display()





    

