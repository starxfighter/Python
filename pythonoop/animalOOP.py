# Set definition of the parent animal class
class Animal():

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print("The health for ", self.name, " is now", self.health)

# Set definition for a child class of animal call Dog
class Dog(Animal):

    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

# set definition for a child class of animal called Dragon
class Dragon(Animal):

    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super().display_health()
        print("I am a Dragon")



# Create animal, walk three times, run twice and then display health
anAnimal = Animal("Bear", 100)
anAnimal.walk().walk().walk()
anAnimal.run().run()
anAnimal.display_health()

# Create a dog, walk three times,run twice, pet and then display health
poodle = Dog("Fluffy", 100)
poodle.display_health()
poodle.walk().walk().walk()
poodle.run().run()
poodle.pet()
poodle.display_health()

# Create a dragon, walk three times, run twice, fly and then display health
oldDragon = Dragon("Drago", 100)
oldDragon.display_health()
oldDragon.walk().walk().walk()
oldDragon.run().run()
oldDragon.fly()
oldDragon.display_health()