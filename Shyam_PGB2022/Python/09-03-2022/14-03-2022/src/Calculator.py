import re

class FormulaError(Exception):
    def __init__(self, msg):
        self.msg = msg

def Calculate(l):
    try:
        regex = r'(\+|-)'

        if(len(l) != 3):
            raise FormulaError

        try:
            a = float(l[0])
            b = float(l[2])
        except ValueError as e:

            raise FormulaError("The first and last arguments must be numbers!") from e


        if(not re.fullmatch(regex, l[1])):
            raise FormulaError("Error: Enter either + or - in the middle!")

        if(l[1] == "+"):
            print("Result: ", a+b )
        if (l[1] == "-"):
            print("Result: ", a-b)

    except FormulaError as e:
        print(e.msg)

while(True):
    l = list(input('\nEnter Formula (Type "quit" to exit): ').split())
    if(l[0] == "quit"):
        exit()
    Calculate(l)

