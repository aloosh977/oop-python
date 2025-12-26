class Number:
    def __init__(self, number: int):
        self.number = int(number)


class SimpleCalc(Number):
    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        try:
            return self.number / other.number
        except ZeroDivisionError:
            return "Cannot divide by zero"


num10 = SimpleCalc(10)
num2 = SimpleCalc(2)
print(num10 + num2)
print(num10 - num2)
num3 = SimpleCalc(3)
num0 = SimpleCalc(0)
print(num2 * num3)
print(num3 / num2)
print(num3 / num0)


class AdvancedCalc(SimpleCalc):
    def __mod__(self, other):
        return self.number % other.number

    def __pow__(self, other):
        return pow(self.number, other.number)


num54 = AdvancedCalc(54)
num15 = AdvancedCalc(15)
num4 = AdvancedCalc(4)
print(num54 % num15)
print(num4**num15)
