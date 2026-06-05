class car:
    def __init__(self, color, mileage):
        self.color=color
        self.mileage = mileage
    
    def description(self):
        print(f"The {self.color} has {self.mileage} miles")
    
    def __str__(self):
        return f"The {self.color} has {self.mileage} miles"
blue_car= car("blue",20000)
red_car = car("red", 30000)
print(blue_car)
print(red_car)
