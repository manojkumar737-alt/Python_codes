class Car:
    colur = "red"
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")
class ToyotaCar(Car):
    def __init__(self, model):
        self.model = model

car1 = ToyotaCar("Corolla")
car2 = ToyotaCar("Camry")

print(car1.start())  # Output: Corolla
print(car2.colur)