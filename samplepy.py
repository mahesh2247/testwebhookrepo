class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b if self.b != 0 else "Cannot divide by zero"


class AdvancedCalculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def subtract(a, b=0):
        return a - b

    @staticmethod
    def multiply(a, b=1):
        return a * b

    @staticmethod
    def divide(**kwargs):
        return kwargs.get("a", 0) / kwargs.get("b", 1) if kwargs.get("b", 1) != 0 else "Cannot divide by zero"


calc = Calculator(10, 5)
print(calc.add())
print(calc.subtract())
print(calc.multiply())
print(calc.divide())

adv_calc = AdvancedCalculator()
print(adv_calc.add(1, 2, 3, 4))
print(adv_calc.subtract(10))
print(adv_calc.multiply(6))
print(adv_calc.divide(a=20, b=4))


