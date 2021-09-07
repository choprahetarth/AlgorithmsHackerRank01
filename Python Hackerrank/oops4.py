# Credits - https://www.youtube.com/watch?v=JeznW_7DlB0&ab_channel=TechWithTim
# how classes deal with each other 
class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age 
        self.grade = grade
    
    def get_name(self):
        return (self.name)

    def get_grade(self):
        return (self.grade)

# create another class 

class Course:
    # add a maximum threshold of students
    # and add only that amount of student objects 
    # inside this class
    def __init__(self,name,max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    # create a method to append the students
    # which takes the student object as a parameter
    def append_students(self,student):
        # student object as parameter 
        self.student = student
        # append till the target is met 
        if(len(self.students)<self.max_students):
            self.students.append(student)
            return True
        return False
    
    def get_students(self):
        return (self.students)
    
    # make a method to calculate the average 
    def calculate_average(self):
        value = 0 
        for student in self.students:
            value += student.get_grade() 
        return (value/len(self.students))


# Create three students  
s1 = Student("Dre",45,95)
s2 = Student("Shady",33,86)
s3 = Student("Convict",23,76) 

# Create a course with max 2 students
c1 = Course("Mathematics", 2) 

# append the students 
print(c1.append_students(s1))
print(c1.append_students(s2))
# you can see that you are unable to add
# more students than 2
print(c1.append_students(s3))

# get students and
print(c1.get_students()) 
# get the first student and 
print(c1.get_students()[0])
# get the first name of the first student 
print(c1.get_students()[0].get_name())


print(c1.calculate_average())