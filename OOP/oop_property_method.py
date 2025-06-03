class Student:
    def __init__(self, py, chem, math):
        self.py = py
        self.chem = chem
        self.math = math

    @property
    def average(self):
        return str((self.py + self.chem + self.math) / 3) + "%"
Stu1 = Student(80, 70, 85)
print("Average marks of student 1 is: " + Stu1.average)
