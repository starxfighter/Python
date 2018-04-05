#Creat a math class
class MathDojo():

    def __init__(self):
        self.val1 = 0
        self.val2 = 0
        self.total = 0

    def add(self, *nums):
        for num in nums:
            self.total += int(num)
        # self.total += (a + b)
        return self

    def subtract(self, *nums):
        for num in nums:
            self.total -= int(num)
        # self.total = self.total - (a + b)
        return self
    
    def result(self):
        print("The total is: ", self.total)


md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result()
