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