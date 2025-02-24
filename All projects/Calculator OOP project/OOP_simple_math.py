"""
    Hello and thanks because you take a look on this script!
    This script, its a simple calculator on console, where, is used a class (OOP method).
    Follow me on GitHub and TikTok(@robert_de_romania) to support me if you want :)
"""

nums = []
input_value = 0

add_operations = ["+","add","plus","addition","adaugă","adună"]
minus_operations = ["-","minus","less","scade","scăzut"]
divide_operations = [":","/","divide","împărțit","împarte"]
multiple_operations = ["*","x","îmulțit","multiple","multipled"]
average_operations = ["avr","average","general","media","medie"]
find_procent_operations = ["%","%i","%1","1%","procent","procent1","1procent","procentaj","procentaj1","1procentaj"]
find_number_operations = ["%ii","%2","2%","procent2","procentaj2","2procent","procentaj2","2procentaj"]
all_operations = [add_operations,minus_operations,divide_operations,multiple_operations,average_operations,find_procent_operations,find_number_operations]

class Calculator:
    def __init__(self,operator,numbers):
        self.operator = operator.lower()
        self.numbers = numbers
        self.result = 0
    def add(self):
        if self.operator in add_operations:
            self.result += sum(self.numbers)
            print(f"{self.result:.2f}")
    def minus(self):
        if self.operator in minus_operations:
            self.result += self.numbers[0] * 2
            for i in self.numbers:
                self.result -= i
            print(f"{self.result:.2f}")
    def divide(self):
        if self.operator in divide_operations:
            first = True
            for i in self.numbers:
                if first:
                    self.result = i
                    first = False
                else:
                    self.result /= i
            print(f"{self.result:.2f}")
    def multiple(self):
        if self.operator in multiple_operations:
            self.result = 1
            for i in self.numbers:
                self.result *= i
            print(f"{self.result:.2f}")
    def average(self):
        if self.operator in average_operations:
            numbers_in_total = 0
            for i in self.numbers:
                self.result += i
                numbers_in_total += 1
            self.result = self.result / numbers_in_total
            print(f"{self.result:.2f}")
    def find_procent(self):
        if self.operator in find_procent_operations:
            self.result = self.numbers[0] / self.numbers[1] * 100
            print(f"{self.numbers[0]} of {self.numbers[1]} is {self.result:.2f}%")
    def find_number(self):
        if self.operator in find_number_operations:
            self.result = self.numbers[0] / 100 * self.numbers[1]
            print(f"{self.numbers[0]}% of {self.numbers[1]} is {self.result:.2f}")


selected_operation = str(input("Enter a operation like +,-,x,/,%1 or avr: "))
calculator = Calculator(selected_operation,nums)
if selected_operation in add_operations or selected_operation in minus_operations or selected_operation in divide_operations or selected_operation in multiple_operations or selected_operation in average_operations:
    while True:
        try:
            input_value = float(input("Add a number in your calculator: "))
            nums.append(input_value)
        except ValueError:
            break
elif selected_operation in find_procent_operations:
    input_value = float(input())
    nums.append(input_value)
    input_value = float(input(f"{nums[0]} of ? is ?% "))
    nums.append(input_value)
    calculator.find_procent()
elif selected_operation in find_number_operations:
    input_value = float(input())
    nums.append(input_value)
    input_value = float(input(f"{nums[0]}% of ? is ? "))
    nums.append(input_value)
    calculator.find_number()
else:
    raise ValueError(f"Invalid operation selected. Please run the script again and enter a valid operation: {all_operations}")


calculator.add()
calculator.divide()
calculator.minus()
calculator.multiple()
calculator.average()