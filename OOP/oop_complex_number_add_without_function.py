class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def shownumber(self):
        print(self.real,"i +", self.imag,"j")

    def __add__(self, num2):
        real_part = self.real + num2.real
        imag_part = self.imag + num2.imag
        return Complex(real_part, imag_part)
    def __sub__(self, num2):
        real_part = self.real - num2.real
        imag_part = self.imag - num2.imag
        return Complex(real_part, imag_part)


num1 = Complex(2, 3)
num1.shownumber()

num2 = Complex(4, 5)
num2.shownumber()

num3 = num1 + num2
num3.shownumber()

num4 = num1 - num2
num4.shownumber()