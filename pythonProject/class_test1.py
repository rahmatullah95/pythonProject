# class
class Student:
    roll = ""
    gpa = ""

    # Constructor
    def __init__(self, roll,gpa):
        self.roll = roll
        self.gpa = gpa

    # methods
    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

# object
Rahmat = Student(74,3.04)
# print(isinstance(Rahmat,Student))
# Rahmat.setValue(74,3.04)
Rahmat.display()

shadman = Student(69,3.69)
# print(isinstance(Rahmat,Student))
# shadman.setValue(69,3.69)
shadman.display()