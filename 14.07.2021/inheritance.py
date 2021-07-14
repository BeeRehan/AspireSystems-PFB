class Bank():
	

	__name = "Reserve Bank of India"
	__tax = "the standard 2%"
	

	#print(__name)		

	
	
	def __repr__(self):
		return(f"The bank  name is {self.__name} and the intrest rate is {self.__tax}")


#print(b.__name)


class Iob(Bank):

	def __init__(self,name,tax):
		self.name = name
		self.tax = tax

	
	def __repr__(self):
		return(f"The bank  name is {self.name} and the intrest rate is {self.tax}")

class Sbi(Iob):
	def __init__(self,name,tax):
		self.name = name
		self.tax = tax

	
	def __repr__(self):
		return(f"The bank  name is {self.name} and the intrest rate is {self.tax}")

class Canara(Iob,Bank):
	def __init__(self,name,tax):
		self.name = name
		self.tax = tax

	
	def __repr__(self):
		return(f"The bank  name is {self.name} and the intrest rate is {self.tax}")

c = Canara("Canara","4%")

print(repr(c))