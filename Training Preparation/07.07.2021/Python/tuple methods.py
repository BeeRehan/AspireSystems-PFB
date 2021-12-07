#Tuble methods

l  = [i for i in range(10)]

t = tuple(l)
print(t)

print("Count: ",t.count(1))

print("indefOf: ",t.index(4))

print("indefOf: ",t.index(4,0,5))
