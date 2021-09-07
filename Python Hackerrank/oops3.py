# Credits - https://www.youtube.com/watch?v=JeznW_7DlB0&ab_channel=TechWithTim
# class instantiate
class dog:
    def __init__(self,name,age):
        self.referal = name
        self.age = age

    # getter methods are used to print
    # the data present
    def get_name(self):
        return self.referal
    
    def get_age(self):
        return self.age

    # these setter functions are 
    # added to modify the existing
    # data, that is stored there
    def set_age(self,age):
        self.age=age
    
    def set_name(self,name):
        self.referal = name
    
d1 = dog("Snoop", 46)
d2 = dog("Dre", 48)

# print existing data
print(d1.get_age())
print(d1.get_name())

# modify data using getter methods
d1.set_age(52)
d1.set_name("Eminem")

# print the modified data 
print(d1.get_age())
print(d1.get_name())
