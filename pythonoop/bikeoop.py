class Bike():
    """Simple Class definition"""

    def __init__(self, price, max_speed):
        self.price = price
        self.speed = max_speed
        self.miles = 0

    def displayInfo(self):
        long_desc = "The cost of the bike is: " + str(self.price) + " and the bike has a top speed of " + str(self.speed) + " The bike has gone " + str(self.miles)
        print(long_desc)

    def ride(self):
        print("Riding")
        self.miles += 10

    def reverse(self):
        print("Reversing")
        self.miles -= 5


new_bike1 = Bike(55, 5)
new_bike1.ride()
new_bike1.ride()
new_bike1.ride()
new_bike1.reverse()
new_bike1.displayInfo()

new_bike2 = Bike(100, 21)
new_bike2.ride()
new_bike2.ride()
new_bike2.reverse()
new_bike2.reverse()
new_bike2.displayInfo()

new_bike3 = Bike(120, 12)
new_bike3.reverse()
new_bike3.reverse()
new_bike3.reverse()
new_bike3.displayInfo()