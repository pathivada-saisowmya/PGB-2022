import re

def num_of_words():
    with open("matter.txt", "r") as file:
        data = file.read()
        print("Total Number of Words in File : ", re.findall(r"[\w']+", data))

num_of_words()

def remove_newline():
    with open("matter.txt", "r") as file:
        data = file.read()
    with open("matter.txt", "w") as file:
        data = data.replace('\n', ' ')
        file.write(data)

remove_newline()

from os import path

def copy_file():
    ifile = input("Enter Source File Name : ")
    if not path.exists(ifile):
        print("Input file Does Not Exists")
        return copy_file()

    ofile = input("Enter Destination File Name : ")
    if path.exists(ofile):
        print("Output File Already Exists")
        return copy_file()

    if ofile == "":
        ofile = "( copy )" + ifile

    with open(ifile, "r") as infile:
        data = infile.read()
    with open(ofile, "w") as outfile:
        outfile.write(data)

copy_file()

import csv

def csv_file():
    csvfile = input("Enter CSV File Name : ")
    with open(csvfile, "rb") as f:
        reader = csv.reader(f)
        headers = next(reader)
        print(f"Total Number of Rows : {len(reader)}")
        print(f"feild Names : {headers}")

csv_file()

def insert_hash():
    with open("matter.txt","r") as file:
        data = file.read()
        for char in data:
            print(char, end="#")
    print()

insert_hash()

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
            import importerror

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
