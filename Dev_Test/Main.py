from Araba import *
from Bayii import *

Car1 = Araba("BMW", "X5", 2025)
Car2 = Araba("Audi", "Q8", 2025)

Car1.printBrand()
Car2.printBrand()


print("Car1: ", Car1.getBrand(), Car1.getMake(), Car1.getYear())

print("Car2: ", Car2.getBrand(), Car2.getMake(), Car2.getYear())

Bayii1 = Bayii(Car1, "Bayerische")
Bayii2 = Bayii(Car2, "Munchen")

print("\n")
Bayii1.showAll()
print("\n")
Bayii2.showAll()