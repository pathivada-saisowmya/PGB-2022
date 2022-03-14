# 2. Design simple calculater application where user input is assumed to be a formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:
#
# 	a. If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
# 	b. Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
# 	c. If the second input is not '+' or '-', again raise a FormulaError
# 	d. If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.

import re

global regex

regex = re.compile(r'[+-/*%]')

class FormulaError(Exception):
    pass


class calculator:
    op = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y,
    }

    def __init__(self):
        self.a = 0
        self.b = 0
        self.operator = ""

    def convert(self, f):
        try:
            self.a = float(f[0])
            self.b = float(f[-1])
            self.operator = f[1]
        except:
            raise FormulaError("Invalid Formula")

    def operator_check(self):
        if re.fullmatch(regex, self.operator):
            pass
        else:
            raise FormulaError("Invalid Formula")


    def calculate(self):
        while True:
            try:
                formula = input("Enter Formula : ")

                if formula == "quit":
                    print("User Exit")
                    break

                formula = formula.split()

                if len(formula) < 3:
                    raise FormulaError("Invalid Formula")

                self.convert(formula)
                self.operator_check()

                print(self.op[self.operator](self.a, self.b))
            except Exception as e:
                print(e)


cal = calculator()
cal.calculate()