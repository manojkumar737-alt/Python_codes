class Car:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("Car is starting")
    @staticmethod
    def stop():
        print("Car is stopping")

class Toyotacar(Car):
        def __init__(self, type, model):
            super().__init__(type)
            self.model = model

        def display(self):
            print(f"Car Type: {self.type}, Model: {self.model}")

car1 = Toyotacar("Sedan", "Camry")
car1.display()
print(car1.type)
Car.start()