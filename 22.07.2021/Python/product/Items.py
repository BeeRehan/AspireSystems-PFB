class Products:
    def __init__(self,products):
        self.products = products
    
    def display(self):
        #return(self.products)
        for product in self.products:
            print(product)
        
    def add(self,product):
        self.products.append(product)
        return(self.products)
            
    def delete(self,id):
        for index,product in enumerate(self.products):
          if(product['id']==id):
            self.products.pop(index)
        self.display()
    
# obj = Products([{
#   "id": "1",
#   "name": "Iphone 11",
#   "product_details": {
#     "ram": "2 GB",
#     "processor": "snapdragon",
#     "screen_size": "4 inch",
#   },
#   "cost": "50000",
#   "currency": "INR",
#   "category": "mobile",
#   "colour": "black"
# },
# {
#   "id": "2",
#   "name": "Samsung Galaxy",
#   "product_details": {
#     "ram": "2 GB",
#     "processor": "snapdragon",
#     "screen_size": "4 inch",
#   },
#   "cost": "45000",
#   "currency": "INR",
#   "category": "mobile",
#   "colour": "grey"
# },
# {
#   "id": "3",
#   "name": "Washing Machine",
#   "product_details": {
#     "machine_capacity": "6kg",
#     "machine_rpm": "50",
#     "type": "top_load"
#   },
#   "cost": "25000",
#   "currency": "INR",
#   "category": "washing-machine",
#   "colour": "blue"
# },
# {
#   "id": "4",
#   "name": "Samsung TV",
#   "product_details": {
#     "isSmart": "false",
#     "resolution": "UHD",
#     "screen_size": "55 inch",
#   },
#   "cost": "40000",
#   "currency": "INR",
#   "category": "tv",
#   "colour": "black"
# }])

# obj.list()
# print(obj.add(1))
# print(obj.delete(0))

