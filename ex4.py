#Numerb of cars available to the shop
Cars = 100
#amount of poeple that can fit in one car
SpaceInCar = 4
#Number if drivers that are on duty today
Drivers = 30
#Number od passangers that need to be transported
Passengers = 90
#number of cars not being driven today
CarsNotDriven = Cars-Drivers
#Number of cars available to be driven today
CarsDriven = Drivers
#
CarPoolCapacity = CarsDriven*SpaceInCar
AveragePassengerPerCar = Passengers / CarsDriven

print("There are", Cars, "cars avalable.")
print("There are only",Drivers,"drivers available")
print("Ther will be",CarsNotDriven,"empty cars today")
print("We can transport",CarPoolCapacity, "poeple today.")
print("We have",Passengers,"to carpool today")
print("We need to put about", AveragePassengerPerCar,"in each car")
