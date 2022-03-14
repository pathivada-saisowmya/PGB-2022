# Write a Python program that reads each row of a given csv file and skip the header of the file. Also print the number of rows and the field names.


f=open('Day4/input.csv','r')

data=f.readlines()
data=data[1:]
print(data)
f.close()