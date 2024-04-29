class Student:
    roll = ""
    gpa = ""

    def setValue(self, roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

Rahmat = Student()
# print(isinstance(Rahmat,Student))
Rahmat.setValue(74,3.04)
Rahmat.display()

shadman = Student()
# print(isinstance(Rahmat,Student))
shadman.setValue(69,3.69)
shadman.display()