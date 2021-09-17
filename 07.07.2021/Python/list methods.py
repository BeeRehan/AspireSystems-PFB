# List

l = [i for i in range(10)]
print("Original: ",l)
l.remove(int(input("Enter the Number want to remove: ")))
print("New List: ",l)

l1 = l.copy()
print("Duplicate-l1: ",l1)

l1.clear()
print("cleared: ",l1)
#print("l-list",l)

l.reverse()
print("Reversed: ",l)

l.sort()
print("Sorted:",l) #also we can use sorted() both are same both have 2 optional parameter

'''
1. reverse = true/false #for decs or asse
2. key = value #factor
'''
