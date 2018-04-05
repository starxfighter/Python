class Product():
    """Simple Class Definition"""

    def __init__(self, price, itemName, weight, brand):
        self.price = price
        self.name = itemName
        self.weight = weight
        self.brand = brand
        self.status = "for sale"


    def sell(self):
        self.status = "sold"
        return self

    def addTax(self, tax):
        total_price = self.price - (self.price * tax)
        return total_price

    def takeReturn(self, retReason):
        if retReason == "defective":
            self.status = "defective"
            self.price = 0
        elif retReason == "like new":
            self.status = "for sale"
        else:
            self.status = "used"
            self.price = self.price - (self.price * .20)

    def display_all(self):
        long_info = ""
        long_info += "Price: " + str(self.price) + "\n"
        long_info += "Item Name: " + self.name + "\n"
        long_info += "Weight: " + str(self.weight) + "lbs\n"
        long_info += "Brand: " + self.brand + "\n"
        long_info += "Status: " + self.status + "\n\n"
        print(long_info)


        
new_prod1 = Product(12.00, "Foobar", 5, "Nike")
new_prod1.sell()
new_prod1.display_all()

new_prod2 = Product(300, "Television", 80, "Sony")
tprice = new_prod2.addTax(.15)
new_prod2.display_all()
print("Total price: ", tprice, "\n")

new_prod3 = Product(100, "Table", 20, "Bush")
new_prod3.takeReturn("defective")
new_prod3.display_all()

new_prod4 = Product(120, "XBOX", 8, "Microsoft")
new_prod4.takeReturn("like new")
new_prod4.display_all()

new_prod5 = Product(19000, "Car", 4000, "Ford")
new_prod5.takeReturn("used")
new_prod5.display_all()