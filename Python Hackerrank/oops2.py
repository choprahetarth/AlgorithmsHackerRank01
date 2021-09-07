# Credits - https://www.youtube.com/watch?v=JeznW_7DlB0&ab_channel=TechWithTim
# class instantiate
class dog:
    def __init__(self,name,age):
        self.referal = name
        self.age = age

    def get_name(self):
        # here you can see that we are 
        # accessing the "global variable"
        # of the class using self
        return self.referal
    
    def get_age(self):
        return self.age

# make two objects of the class
d1 = dog("Snoop",45)
d2 = dog("Dre",48)
# access the variable "referal" of both
# the classes
print(d1.referal)
print(d2.referal)
# access the get_name function
print(d1.get_name())
print(d2.get_name())
# as you can see, we can access the variable

print(d1.get_age())
print(d2.get_age())