from random import randint
import re

global regex

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

class NameNotUnique(Exception):
    pass


class NegativeAge(Exception):
    pass


class AgeNotSufficient(Exception):
    pass


class InvalidEmail(Exception):
    pass


class Student:
    def __init__(self, s_list):
        self.studentList = s_list
        self.student_db = {}
        self.add_to_db()

    def validate_name(self, uname):
        if uname in self.student_db:
            raise NameNotUnique("Username Already Exists")
        pass


    def validate_age(self, age):
        if 16 > age > 0:
            raise AgeNotSufficient("Age Is less than 16")
        if age < 0:
            raise NegativeAge("Age Is Less Than 0")

    def validate_email(self, email, uname):
        if re.fullmatch(regex, email):
            pass
        else:
            raise InvalidEmail("Invalid Email Found")

    def add_to_db(self):
        for student in self.studentList:
            try:
                self.validate_name(student[0])

                self.validate_age(student[-1])

                self.validate_email(student[1], student[0])

                print(f"Student Added To DB : {student[0]}")
                self.student_db[student[0]] = student[1]

            except Exception as e:
                print(e)

test_cases = []

for i in range(30):
    age = randint(15, 22)
    test_cases.append((f"Student{i}", f"Student{i}@test.com", age))

test_cases.append(test_cases[-1])
test_cases.append(("Studentnegative", "Studentnegative@test.com", -10))
test_cases.append(("Studentemail", "Studentemail", 20))
test_cases.append(("Student1", "Studentemail1@test.com", 20))



print(test_cases)
s = Student(test_cases)



