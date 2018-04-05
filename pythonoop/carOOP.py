class Car():
    """Simple Class Definition"""

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()
        
    def display_all(self):
        long_info = ""
        long_info += "Price: " + str(self.price) + "\n"
        long_info += "Speed: " + str(self.speed) + "mph\n"
        long_info += "Fuel: " + self.fuel + "\n"
        long_info += "Mileage: " + str(self.mileage) + "mpg\n"
        long_info += "Tax Rate: " + str(self.tax) + "\n\n"
        print(long_info)

new_car1 = Car(2000, 35, "Full" , 15)
new_car2 = Car(2000, 5, "Not Full", 105)
new_car3 = Car(2000, 15, "Kind of Full", 95)
new_car4 = Car(2000, 25, "Full", 25)
new_car5 = Car(2000, 45, "Empty", 25)
New_car6 = Car(20000000, 35, "Empty", 15)
