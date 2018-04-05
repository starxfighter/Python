import random
import math
# Create Patient class
class Patient():

    def __init__(self, pid, name, allergies):
        self.allergies = []
        self.pid = pid
        self.name = name 
        self.allergies = allergies
        self.bedNum = None
        # print(self)

    def displayPat(self):
        print("pid", self.pid)
        print("name", self.name)
        print("allergies", self.allergies)
        print("bed num", self.bedNum)
        return self

class Hospital():

    def __init__(self, hospname, capacity):
        self.patients = []
        self.hname = hospname
        self.capacity = capacity

    def admit(self, pRec):
        # Assign a bed number
        tempbed = random.random() * 100
        abed = math.floor(tempbed)
        pRec.bedNum = abed
        # Check if capacity reached
        if len(self.patients) < self.capacity:
            self.patients.append(pRec)
        else:
            print("Hospital Full")
      
    def discharge(self, rId):
        index = 0
        for elem in self.patients:
            if elem.pid == rId:
                self.patients.pop(index)
                elem.bedNum = 0
                elem.displayPat()

    def display(self):
        for x in self.patients:
            print("pid", x.pid)
            print("name", x.name)
            print("allergies", x.allergies)
            print("bed num", x.bedNum)
        print("Hosp Name", self.hname)
        print("Capacity", self.capacity)




mercy = Hospital("Mercy Hospital", 4)
pat1 = Patient(303, "Thomas", ["latex", "shellfish"]) 
mercy.admit(pat1)

pat2 = Patient(301, "Betty", ["latex", "shellfish", "iodine"]) 
mercy.admit(pat2)

pat3 = Patient(280, "William", ["none"]) 
mercy.admit(pat3)

pat4 = Patient(102, "Kirk", ["latex", "strawberries"]) 
mercy.admit(pat4)

pat5 = Patient(524, "David", ["latex", "nuts"]) 
mercy.admit(pat5)
mercy.display()
print("Discharging")
mercy.discharge(280)
print("Hospital Check")
mercy.display()