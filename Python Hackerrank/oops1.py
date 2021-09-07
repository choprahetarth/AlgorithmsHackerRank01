# Credits - https://www.youtube.com/watch?v=JeznW_7DlB0&ab_channel=TechWithTim
class dog:
    # initialized method of the class
    # it automatically runs when the 
    # class is initiated
    def __init__(self,name):
        # self.name creates an attribute
        # of the class dog.
        # this is like a global variable 
        # in the scope of the class
        self.name=name
    # method of class with self as the 
    # parameter
    def bark(self):
        print("bark")

    # add another method
    # which returns something
    def add_one(self,x):
        return x+1
        

# instance of the class
# basically we made an object
d = dog("Hello")

# call the first method of the class
d.bark()

# call the second method of the class
# which returns a value that we have to 
# print
print(d.add_one(4))

print (type(d))

# in this output we have 
# <class'__main__.dog'
# here the class is by defualt
# defined in the main module


# self meaning
# what self is doing is that when anytime
# the above methods are called
# an actual reference to the specific dog() 
# object is passed so that we can access that 
# specific object's attributes.

d2 = dog("Bellow")

# here the same class is being used 
# after a different object is passed within it
# and hence a reference is generated.
