d = dict((k,v) for k,v in ([(1,"Yasin"),(2,"Mohamed"),(3,"Aspirian")]))

print(d)

keys = ["yasin","mohamed","aspirian"]
values = [1,2]

a = dict.fromkeys(keys,values)
print(a)

#points to the same reference that's why the dictionary was got affected
values.append(3)
print(a)

print(a.get("yasin"))

print(a.get("yin",1))#take 2 parameter one is key and another one is optional value parameter
#if key is not found the provided value will be returned if the value is not provide then it returned as none.


for k,v in a.items():
	print(k,v)

print(d.keys())
print(d.values())

print(d.pop("Yasin",1))#accepet one main and 1 optional parameter if key not found the given value returned.

print(a.popitem())

print(a.setdefault("yasin"))#accepet one main and 1 optional parameter if key not found the given value returned.


a.update(d)
print(a)#accept iterable with key and value pair
