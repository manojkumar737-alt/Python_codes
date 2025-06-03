class Person:
    name = "Suraj"

    @classmethod
    def change_name(cls, name):
        cls.name = name

p1 = Person()
p1.change_name("Rohit")
print(p1.name)  # Output: Rohit
print(Person.name)  # Output: Rohit