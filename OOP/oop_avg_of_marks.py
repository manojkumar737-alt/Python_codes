class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def avg_marks(self):
        sum1 = sum(self.marks)
        print("Average marks of {} is {}".format(self.name, sum(self.marks) / len(self.marks)))
        print(f"Average marks of {self.name} is {sum1 / len(self.marks)}")

s1 = Student("Alice", [85, 90, 78])
s1.avg_marks()
s2 = Student("Bob", [92, 88, 95])
s2.avg_marks()
s1.name = "manoj"
s1.avg_marks()