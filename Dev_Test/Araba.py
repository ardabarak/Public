class Araba:
	def __init__(self, brand, make, year):
		self.brand = brand
		self.make = make
		self.year = year

	def getBrand(self):
		return (self.brand)
	
	def getMake(self):
		return (self.make)
	
	def getYear(self):
		return (self.year)

	def printBrand(self):
		print(self.brand)
	
	def printMake(self):
		print(self.make)
	
	def printYear(self):
		print(self.year)

