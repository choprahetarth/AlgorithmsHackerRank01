# Credits - https://www.youtube.com/watch?v=JeznW_7DlB0&ab_channel=TechWithTim
# inheritance and method overriding 
# and Super() keyword
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

    # add a same method as the child classes
    def speak(self):
        print("I Don't know what to say ")
 
class Dog(Pet):
    def speak(self):
        print("Bark")

# suppose we have to modify one inherited class's parameters  
# without re-initializing  the previous parameters
class Cat(Pet):
    def __init__(self,name,age,color):
        # Super keyword mentions the above class,
        # and the .__init__ method is called of parent class
        # where you pass the parameters name and age.
        # no need to pass self as we are doign that in the parent class 
        super().__init__(name,age)
        self.color=color

    def speak(self):
        print("Meow")
    
    def get_color(self):
        return(self.color)

class Fish(Pet):
    pass

p1 = Pet("Jim",2)
d1 = Dog("Messi",10)
c1 = Cat("Kittles",11,"Blue")
f1 = Fish("Bubbles",3)

p1.speak()
# The speak is overriden by the method defined
# in the child class
d1.speak()
c1.speak()
# but when there is no child method, it automatically
# goes to the parent method
f1.speak()

print(c1.get_color())