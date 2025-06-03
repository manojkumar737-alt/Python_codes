class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def showDetails(self):
        print(f"Role: {self.role}, Department: {self.dept}, Salary: {self.salary}")
    
class Manager(Employee):
    def __init__(self, role, dept, salary, team_size):
        super().__init__(role, dept, salary)
        self.team_size = team_size
    def showDetails(self):
        super().showDetails()
        print(f"Team Size: {self.team_size}")
class Engineer(Employee):
    def __init__(self, role, dept, salary, expertise):
        super().__init__(role, dept, salary)
        self.expertise = expertise
    def showDetails(self):
        super().showDetails()
        print(f"Expertise: {self.expertise}")

Engineer1 = Engineer("Software Engineer", "IT", 80000, "Python")
Engineer1.showDetails()
Manager1 = Manager("Project Manager", "IT", 90000, 5)
Manager1.showDetails()
Manager2 = Manager("HR Manager", "HR", 85000, 3)
Manager2.showDetails()