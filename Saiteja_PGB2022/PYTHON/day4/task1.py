#Write a simple program which loops over a list of user data (tuples containing a username, email and age) and adds each user to a dictionary if the user is at least 16 years old. You do not need to store the age. Write a simple exception hierarchy which defines a different exception for each of these error conditions:
#a. the username is not unique
#	b. the age is not a positive integer
#	c. the user is under 16
#	d. the email address is not valid (a simple check for a username, the @ symbol and a domain name is sufficient)
#	e. Raise these exceptions in your program where appropriate. Whenever an exception occurs, your program should move onto the next set of data in the list. Print a different error message for each different kind of exception.
class DuplicateUsernameError(Exception):
    pass
class InvalidAgeError(Exception):
    pass
class UnderageError(Exception):
    pass
class InvalidEmailError(Exception):
    pass

# A class for a user's data
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

example_list = [
    ("pritam", "pritam@example.com", 21),
    ("astra", "astra@example", 19),
    ("diablo", "jane2@example.com", 25),
    ("steoamon", "steve@somewhere", 15),
    ("viper", "sage", 23),
    ("sage", "sage@example.com", -3),
]
directory = {}
for username, email, age in example_list:
    try:
        if username in directory:
            raise DuplicateUsernameError()
        if age < 0:
            raise InvalidAgeError()
        if age < 16:
            raise UnderageError()
        email_parts = email.split('@')
        if len(email_parts) != 2 or not email_parts[0] or not email_parts[1]:
            raise InvalidEmailError()
    except DuplicateUsernameError:
        print("Username '%s' is in use." % username)
    except InvalidAgeError:
        print("Invalid age: %d" % age)
    except UnderageError:
        print("User %s is underage." % username)
    except InvalidEmailError:
        print("'%s' is not a valid email address." % email)
    else:
        directory[username] = User(username, email)

#Design simple calculater application where user input is assumed to be a formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:
#	a. If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
#	b. Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
#	c. If the second input is not '+' or '-', again raise a FormulaError
#	d. If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.
class FormulaError(Exception): pass
def parse_input(user_input):
  input_list = user_input.split()
  if len(input_list) != 3:
    raise FormulaError('Input does not consist of three elements')
  n1, op, n2 = input_list
  try:
    n1 = float(n1)
    n2 = float(n2)
  except ValueError:
    raise FormulaError('The first and third input value must be numbers')
  return n1, op, n2
def calculate(n1, op, n2):
  if op == '+':
    return n1 + n2
  if op == '-':
    return n1 - n2
  if op == '*':
    return n1 * n2
  if op == '/':
    return n1 / n2
  raise FormulaError('{0} is not a valid operator'.format(op))
while True:
  user_input = input('>>> ')
  if user_input == 'quit':
    break
  n1, op, n2 = parse_input(user_input)
  result = calculate(n1, op, n2)
  print(result)

#Write a Python program that takes a text file as input and returns the number of words of a given text file.
def num_of_words(filepath):
    with open(filepath)as f:
        data=f.read()
        data.replace(","," ")
        return len(data.split(" "))
print(num_of_words("sample.txt"))

#Write a Python program to remove newline characters from a file
def remove_newline(fname):
    fileobj=open(fname).readlines()
    return [s.rstrip('/n') for s in fileobj]
print(remove_newline("sample.txt"))

#Write a Python program to copy the contents of a file to another file .
import shutil
shutil.copyfile('sample.txt','sample2.txt')

#Write a Python program that reads each row of a given csv file and skip the header of the file. Also print the number of rows and the field names.
import csv
fields = []
rows = []
with open('samplecsv.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar=',')

 # Following command skips the first row of the CSV file.
 fields = next(data)
 for row in data:
   print(', '.join(row))
print("\nTotal no. of rows: %d"%(data.line_num))
print('Field names are:')
print(', '.join(field for field in fields))

#Write a Python program that reads each row of a given csv file and skip the header of the file. Also print the number of rows and the field names.
#A text file named "matter.txt" contains some text, which needs to be displayed such that every next character is separated by a symbol "#".
#	Write a function definition for hash_display() in Python that would display the entire content of the file matter.txt in the desired format.
#	Example :
#	If the file matter.txt has the following content stored in it :
#	THE WORLD IS ROUND
def hash_displayfun():
    with open("matter.txt","r") as file:
        data = file.read()
        for char in data:
            print(char, end="#")
    print()
hash_displayfun()

#Write a class to handle below exceptions
	# a. ZeroDivisionError
    # b. ImportError
	# c. IndexError
	# d. IndentationError
	# e. ValueError
	# f. Exception
	# g. Raise any exception and handle it properly and use else, finally blocks to print something irrespective of exception
class CustomException(Exception):
    pass
class ExceptionHandling:
    def __init__(self):
        self.ZeroDivisionError_Handler()
        self.ImportError_Handler()
        self.IndexError_Handler()
        self.IndentationError_Handler()
        self.ValueError_Handler()
        self.CustomException_Handler()
        self.else_finally_Handler()
    def ZeroDivisionError_Handler(self):
        try:
            a = 1 / 0
        except ZeroDivisionError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def ImportError_Handler(self):
        try:
            from re import notexistingmethod
        except ImportError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def IndexError_Handler(self):
        l = ["a"]
        try:
            print(l[3])
        except IndexError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def IndentationError_Handler(self):
        try:
            import exception1

        except IndentationError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def ValueError_Handler(self):
        valerr = input("Enter String : ")
        try:
            int(valerr)
        except ValueError as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def validate(self, t):
        if t < 20:
            raise CustomException("This is an custom Exception")

    def CustomException_Handler(self):
        test = 16
        try:
            self.validate(test)
        except CustomException as e:
            print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")

    def else_finally_Handler(self):
        for i in range(5, 0, -1):
            try:
                a = int(input("Enter 1st Number : "))
                b = int(input("Enter 2nd Number : "))
                output = a // b
            except Exception as e:
                print(f"Error Name : {e.__class__.__name__}" + "\n" + f"Error Message : {e}")
            else:
                print(f"Output is : {output}")
            finally:
                print(f"{i-1} Chances Left")

ExceptionHandling()