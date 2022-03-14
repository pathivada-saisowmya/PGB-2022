#defining variables for each datatype
empid = 101
empname = "ramu"
empsalary = 1000.50
print(empid)
print(empname)
print(empsalary)
print(type(empid))
print(type(empname))
print(type(empsalary))
#modify the data and identify which data types are mutable and which are immutable
emplist = ["ram" , "rahul" , "sai"]
emplist[0]="sita"
print(emplist)
emptupple =("ram" , "rahul" , "sai")
#emptupple[0]='sita'
#print(emptupple)
#Creating variable and assign multiple values and override the data types
empvar=10
empvar="ram"
empvar=100.10
print(empvar)
#Define variable 'a' and store int and string types using + operator
a = str(101) + "ram"     #resolved by typecasting
print(a)
#define variable 'b' and store string and boolean types using + operator
b = "ram" + str(True)    #resolved by typecasting
print(b)
#define variable 'c' and store list and tuple types using + operator
c = emplist + list(emptupple)
print(c)
#create a list fruits = ['apple', 'banana', 'cherry'], cars = ['Ford', 'BMW', 'Volvo'] and apply respective inbuilt method to
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
#Add an element to the fruits list
fruits.append('gova')
print(fruits)
#Remove all elements from the fruits list
fruits.clear()
print(fruits)
#Copy the fruits list
num=fruits.copy()
print(num)
#Return the number of times the value "cherry" appears in the fruits list
cnt=fruits.count("cherry")
print(cnt)
#Add the elements of cars to the fruits list
fruits.extend(cars)
print(fruits)
fruits = ['apple', 'banana', 'cherry']
#What is the position of the value "cherry"
ind=fruits.index("cherry")
print(ind)
#Insert the value "orange" as the second element of the fruit list
fruits.insert(1,"orange")
print(fruits)
#Remove the second element of the fruit list
fruits.pop(1)
print(fruits)
#Remove the "banana" element of the fruit list
fruits.remove("banana")
print(fruits)
#Reverse the order of the fruit list
fruits.reverse()
print(fruits)
#Sort the cars list
cars.sort()
print(cars)
#Create a string
company="comakeit"
#Convert it into upper case
up=company.upper()
print(up)
#Convert into lower case
lo=company.lower()
print(lo)
#Return the number of times a specified value occurs in a string
print(company.count('a'))
#Return true if the string ends with the specified value
print(company.endswith('c'))
#Return True if all characters in the string are in the alphabet
print(company.isalpha())
#Convert the first character of each word to upper case
company="comakeit company company"
print(company.title())
#Convert the first character to upper case
print(company.capitalize())
#Search the string for a specified value and returns the position of where it was found
print(company.index("company"))
#Reverse the string with slicing
company="comakeit company company"[::-1]
print(company)
#Create a tuple
sampletupple =("ram" , "rahul" , "sai","sai")
#Return the number of times a specified value occurs in a tuple
print(sampletupple.count("sai"))
#Search the tuple for a specified value and returns the position of where it was found
print(sampletupple.index("sai"))
#Create a dictionary with 3 different keys, all with the value '5' using inbuilt method
empdictionary = {
  "empid": 5,
  "empname": 5,
  "empsalary": 5
}
print(empdictionary)
#Create a dictionary  and and apply respective inbuilt method to
empdictionary = {
  "empid": 5,
  "empname": 5,
  "empsalary": 5
}
#Return the value of the specified key
print(empdictionary["empid"])
#Print all key, value pairs
print(empdictionary)
#Remove the element with the specified key
empdictionary.pop("empid")
print(empdictionary)
#Remove the last inserted key-value pair
empdictionary.popitem()
print(empdictionary)
#Create a Set and apply inbuild methods to
myset = {"apple", "banana", "cherry"}
print(myset)
#Add an element to the set
myset.add("orange")
print(myset)
#Remove specific element
myset.remove("orange")
print(myset)
#create 2 sets x and y and
myset2 = {"ram", "sai", "sita", "apple", "cherry"}
#Return a set that contains the items that only exist in set x, and not in set y
print(myset-myset2)
#Remove the items that exist in both sets
unions=myset.union(myset2)
common = myset.intersection(myset2)
myset=myset-common
myset2=myset2-common
print(myset)
print(myset2)
#Return True if no items in set x is present in set y
print(myset.isdisjoint(myset2))
#Return True if all items in set x are present in set y
print(myset.issubset(myset2))
#Return True if all items set y are present in set x
print(myset2.issubset(myset))
#Return a set that contains all items from both sets, except items that are present in both sets
sampleset=unions-common
print(sampleset)
#Remove the items that are present in both sets, AND insert the items that is not present in both sets
print(myset.symmetric_difference_update(myset2))
#Return a set that contains all items from both sets, duplicates are excluded
print(myset.union(myset2))
#Insert the items from set y into set x
myset.update(myset2)
print(myset)