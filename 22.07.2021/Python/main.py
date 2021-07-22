from product.Items import *

def init():
    global add, view, delete 
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
    
    add  = obj.add
    view = obj.display
    delete = obj.delete


init()

def select(msg):
    return(input(msg))

def addMobile():
    product = dict()
    #print(product)
    product['id'] = input("Enter the ID: ")
    product['name'] = input("Enter the Name: ")
    product.update({'product_details':{'ram':input("Enter the Ram: "),'processor':input("Enter the processor: "),'screen_size':input("Enter the screensize: ")}})
    product['cost'] = input("Enter the cost: ")
    product['currency'] = input("Enter the currency: ")
    product['category'] = input("Enter the category: ")
    product['colour'] = input("Enter the colour: ")
    
    add(product)
    view()
    #print(product)

def addWashingMachine():
    product = dict()
    #print(product)
    product['id'] = input("Enter the ID: ")
    product['name'] = "Washing Machine"
    product.update({'product_details':{'machine_capacity:':input("Enter the machine_capacity: "),'machine_rpm':input("Enter the machine_rpm: "),'type':input("Enter the type: ")}})
    product['cost'] = input("Enter the cost: ")
    product['currency'] = input("Enter the currency: ")
    product['category'] = input("Enter the category: ")
    product['colour'] = input("Enter the colour: ")
    add(product)
    view()

def addTV():
    product = dict()
    #print(product)
    product['id'] = input("Enter the ID: ")
    product['name'] = input("Enter the Name: ")
    product.update({'product_details':{'isSmart':input("Enter the isSmart: "),'resolution':input("Enter the resolution: "),'    ':input("Enter the screensize: ")}})
    product['cost'] = input("Enter the cost: ")
    product['currency'] = input("Enter the currency: ")
    product['category'] = input("Enter the category: ")
    product['colour'] = input("Enter the colour: ")
    add(product)
    view()

def addProduct():
    print("1. Mobile \n2. Washing Machine\n3. TV ")
    ch = input()
    
    if(ch =='1'):
        addMobile()
    elif(ch =='2'):
        addWashingMachine()
    elif(ch=='3'):
        addTV()


def deleteProduct():    
    id = input("Enter the id: ")
    delete(id)


def admin():
    view()

    while True:
        print("1. Add Product \n2. Delete Product")
        ch = input()

        if(ch=='1'):
            addProduct()
        elif(ch=='2'):
            deleteProduct()




def customer():
     print("Under Construction!!!")


while True:
    print("Who are you?")
    print("1. Admin \n2. Customer")
    ch = input()
    if(ch=='1'):
        admin()
    elif(ch=='2'):
        customer()


#dispaly()

# if __name__ == '__main__':
#     print("Welcome!!!")
#     init()
# else:
#     print("!!!")
#     print("Imported")