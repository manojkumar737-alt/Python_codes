class Student:
    college_name = "ABC University"
    def __init__(self, name, age, Marks):
        self.name = name
        self.age = age
        self.Marks = Marks
    def welcome(self):
        print(f"Welcome {self.name} to {self.college_name}!")   
    def grade(self):
        if self.Marks >= 90:
            return "A"
        elif self.Marks >= 80:
            return "B"
        elif self.Marks >= 70:
            return "C"
        elif self.Marks >= 60:
            return "D"
        else:
            return "F"

s1 = Student("Alice", 20, 85)
s1.welcome()
print(f"Total marks {s1.Marks} of {s1.name} and has a grade of {s1.grade()}.")
s2 = Student("Bob", 22, 92)
s2.welcome()
print(f"Total marks {s2.Marks} of {s2.name} and has a grade of {s2.grade()}.")