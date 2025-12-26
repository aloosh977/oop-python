class Operation:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number


class SimpleCalc(Operation):
    def __add__(self):
        return self.first_number + self.second_number

    def add(self):
        return self.first_number + self.second_number

    def subtract(self):
        return self.first_number - self.second_number

    def multiply(self):
        return self.first_number * self.second_number

    def divide(self):
        try:
            return self.first_number / self.second_number
        except ZeroDivisionError:
            return "Error: Cannot divide by zero"


first_number = 10
second_number = 0
calc = SimpleCalc(first_number, second_number)
print(calc.divide())
calc = SimpleCalc(56566542999, 49545646651)
print(calc.multiply())


class AdvancedCalc(SimpleCalc):
    def modulo(self):
        return self.first_number % self.second_number

    def power(self):
        return pow(self.first_number, self.second_number)


advCalc = AdvancedCalc(first_number, second_number)
print(advCalc.power())
advCalc = AdvancedCalc(157, 234)
print(advCalc.power())
