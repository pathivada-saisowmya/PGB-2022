#Writing a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.
import datetime
def calculation(a,b):
    c = a+b
    d = a-b
    return c,d
res = calculation(4,5)
print(res)

#Write a program to create a function show_employee() using the following conditions.
#It should accept the employee’s name and salary and display both.
#If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(empname,empsalary=9000):
    return empname,empsalary
empdetails=show_employee("ram",)
print(empdetails)

#Create an inner function to calculate the addition in the following way
#Create an outer function that will accept two parameters, a and b
#Create an inner function inside an outer function that will calculate the addition of a and b
#At last, an outer function will add 5 into addition and return it
def outterfun(a,b):
    def innerfun():
        return a+b
    return 5+innerfun()
ans=outterfun(2,5)
print(ans)

#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
def recursivefun(n):
    if n>0:
        return n+recursivefun(n-1)
    else:
        return 0
rec=recursivefun(10)
print(rec)

#Assign a different name to function and call it through the new name Ex: Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.
newfunname=recursivefun
print(newfunname(11))

#Find the largest item from a given list without using inbuilt methods
samplelist = [1,3,10,20,5,100]
temp=0
for i in range(len(samplelist)):
    if(temp<samplelist[i]):
        temp=samplelist[i]
print(temp)

#Convert string into a datetime object
#	Input : date_string = "Mar 09 2022 11:20AM"
#	output: 2022-03-09 11:20:00
date_string = "Mar 09 2022 11:20AM"
datetime_object = datetime.datetime.strptime(date_string,'%b %d %Y %I:%M%p')
print(datetime_object)

#Calculate the date 4 months from the current date
print(datetime.datetime.today()+ datetime.timedelta(4*365/12))

#Generate 6 digit random secure OTP
import random
otp_obj = random.randint(100000, 999999);
print("OTP:", otp_obj);

#Generate a random Password which meets the following conditions
#	a. Password length must be 10 characters long.
#	b. It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
import random
import string
def generate_password(length=10):
    two_random_uppercase = random.choices(string.ascii_uppercase, k=2)
    other_random_characters = random.choices(
        string.ascii_lowercase + string.digits + string.punctuation,
        k=length - 2,
    )

    password = "".join(
        random.sample(two_random_uppercase + other_random_characters, k=length)
    )

    return password


print(generate_password())
#Write a program to use for loop to print the following reverse number pattern
rows=5
for i in range(0,rows+1):
    for j in range(rows-i,0,-1):
        print(j,end=' ')
    print()

#Count all letters, digits, and special symbols from a given string
samplestr="saiteja2808@gmail.com"
alphabets = digits = special = 0
for i in range(len(samplestr)):
    if (samplestr[i].isalpha()):
        alphabets = alphabets + 1
    elif (samplestr[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1

print("Total Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)

#Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
s1="sai"
s2="teja"
length1=len(s1)
length2=len(s2)
if length1>length2:
    length=length1
else:
    length=length2
s2=s2[::-1]
s3=""
for i in range(length):
    if i < length1:
        s3 = s3 + s1[i]
    if i < length2:
        s3 = s3 + s2[i]
print(s3)

#Write a program to remove special symbols / punctuation from a string
#	Ex : str1 = "/*We are le@arning python@67 fun_da**mentals**"
#	Output: We are learning python fundamentals
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str1 = "/*We are le@arning python@67 fun_da**mentals**"
# remove punctuation from the string
no_punct = ""
for char in my_str1:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print("Display the unpunctuated string: ",no_punct)

#Write a program to removal all characters from a string except integers
#	Input : str1 = 'I am 20 years and and 22 months old'
#	Output : 2022
str1="I am 20 years and and 22 months old"
getVals = list([val for val in str1
               if val.isnumeric()])

result = "".join(getVals)
print(result)

#Write a program to find words with both alphabets and numbers from an input string.
#	Input : str1 = "Sriman25 is Data scientist50 and AI Expert"
#	Output : ['Sriman25','Scientist50']
samplestring1=["Sriman25 is Data scientist50 and AI Expert"]
for i in samplestring1:
    for j in i.split(' '):
        if j.isalnum() and not j.isalpha() and not j.isdigit():
            print(j)