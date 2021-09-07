# Credits - https://www.youtube.com/watch?v=JeznW_7DlB0&ab_channel=TechWithTim
# inheritance 
# Create a parent class
class Pet:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
        print("A new pet has been added")

    def get_name(self):
        return (self.name)
    
    def get_age(self):
        return (self.age)

# Create a child class, 
# that will basically inherit all methods and 
# variables of the parent class    
class Dog(Pet):
    def speak(self):
        print("Bark")

# Create another child class,
# that will also have al methods and variables of 
# the parent class 
class Cat(Pet):
    def speak(self):
        print("Meow")

# Instantiate the parent class via the child class
d1 = Dog("Messi",10)
# invoke child class's method
d1.speak()
# invoke parent class's method via child class 
print(d1.get_name())
# invoke parent class's variable via child class 
print(d1.age)

