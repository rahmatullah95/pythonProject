class Student:
    roll = ""
    gpa = ""

Rahmat = Student()
# print(isinstance(Rahmat,Student))
Rahmat.roll = 74
Rahmat.gpa = "3.04"
print(f"Roll: {Rahmat.roll}, GPA: {Rahmat.gpa}")

shadman = Student()
# print(isinstance(Rahmat,Student))
shadman.roll = 69
shadman.gpa = "3.69"
print(f"Roll: {shadman.roll}, GPA: {shadman.gpa}")