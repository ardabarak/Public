from Araba import *

class Bayii:
	def __init__(self, Araba, bayii):
		self.brand = Araba.getBrand()
		self.make = Araba.getMake()
		self.year = Araba.getYear()
		self.bayii = bayii
	
	def getBayii(self):
		return self.bayii
	
	def showAll(self):
		print("Car and Dealer info:")
		print("Brand:	", self.brand, 
			"\nMake:	", self.make, 
			"\nYear:	", self.year, 
			"\nDealer:	", self.bayii)
