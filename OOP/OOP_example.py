class Student:
    #default constructors
    def __init__(self):
        pass
    #parameterized constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("adding student:", self.name, "age:", self.age)

s1 = Student("John", 20)
print(s1.name, s1.age)
s2 = Student("Alice", 22)
print(s2.name, s2.age)