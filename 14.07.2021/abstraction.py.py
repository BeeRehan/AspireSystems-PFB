from abc import ABC

class Base(ABC):
	def find(self):
		pass


class Emp(Base):
	def where(self):
		print("This is where?")

	
	def find(self):
		print("This is me..")


e = Emp()

e.where()
e.find()