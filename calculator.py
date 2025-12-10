class Calculator:
    def __init__(self,first_number,second_number):
        self.first_number=first_number
        self.second_number=second_number

class SimpleCalc(Calculator):
    def add(self):
        return self.first_number+self.second_number
    def subtract(self):
        return self.first_number-self.second_number
    def multiply(self):
        return self.first_number*self.second_number
    def divide(self):
        return self.first_number/self.second_number

first_number=10
second_number=5
calc=SimpleCalc(first_number,second_number)
print(calc.add())
