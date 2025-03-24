# Student num - B00154235
# Class Vehicle
# Init Attributes name, year, max_speed, mileage, colour

import math
from datetime import date

class vehicle :
    #Creating an init method
    def __init__(self, name, year, max_speed, mileage, colour):
        self.name = name
        self.year = year
        self.max_speed = max_speed
        self.mileage = mileage
        self.colour = colour

    def max_speed(self):
        return 2*math.pi * self.max_speed
    
    def mileage(self):
        return 2*math.pi * self.mileage
    # ROUGH WORK 
    # # Method for the name
    # def name(self, name):
    #     this.name = name
    # # Method for the year
    # def year(self, year):
    #     this.year = year
    # #Method for the maxspeed
    # def max_speed(self, max_speed):
    #     this.max_speed = max_speed
    # #methoed for the mileafe
    # def mileage(self, mileage):
    #     this.mileage = mileage
    # #Method for the colour
    # def colour(self, colour):
    #     this.colour = colour

vehicle = vehicle ("Mini Cooper", (2020, 5, 11), "8.5kmph", "100500", "red")
print(f"Car name {vehicle.name} year {vehicle.year} max speed {vehicle.max_speed} max speed {vehicle.mileage} colour {vehicle.colour}")