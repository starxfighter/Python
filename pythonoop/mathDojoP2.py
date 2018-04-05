#Creat a math class
class MathDojo():

    def __init__(self):
        self.total = 0

    def add(self, *args):
        for arg in args:
            if isinstance(arg, list) or isinstance(arg, tuple):
                for e in arg:
                    self.total += int(e)
            elif isinstance(arg, int) or isinstance(arg, float):
                    self.total += arg
        return self

    def subtract(self, *args):
        for arg in args:
            if isinstance(arg, list) or isinstance(arg, tuple):
                for e in arg:
                    self.total -= int(e)
            elif isinstance(arg, int) or isinstance(arg, float):
                    self.total -= arg
        return self
    
    def result(self):
        print("The total is: ", self.total)

md = MathDojo()
md.add([1], 3,4).result()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).result()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()