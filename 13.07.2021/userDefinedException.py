class Error(Exception):
	def __init__(self,msg):
		self.msg = msg

try:
	#print(10/0)
	if(int(input("Enter Your age: "))>=18):
		print("Can be vote")
	else:
		raise(Error("Below 18 can't be vote"))
except Error as e:
	print("Warning--> Age limit: ",e.msg)

finally:
	print("End of test")
