"""import csv
with open('sample.csv', 'r') as file:
    reader= csv.reader(file,delimiter=',')
    #print("number of rows in csv file",len(list(reader)))
    next(reader)
    for row in reader:
        print(row)
    columns=[]
    for row in reader:
        columns.append(row)
        break
print(columns[0])"""


"""import csv
 
# opening the csv file by specifying
# the location
# with the variable name as csv_file
with open('sample.csv') as file:
 
    # creating an object of csv reader
    # with the delimiter as ,
    reader = csv.reader(file, delimiter = ',')
    next(reader)
    for row in reader:
        print(row)
 
    # list to store the names of columns
    column_names = []
 
    # loop to iterate through the rows of csv
    for row in reader:
 
        # adding the first row
        column_names.append(row)
 
        # breaking the loop after the
        # first iteration itself
        break
 
# printing the result
print("List of column names : ",
      column_names[0])"""
import csv
fields = []
rows = []
with open('sample.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar=',')
 # Following command skips the first row of the CSV file.
 fields = next(data)
 for row in data:
   print(', '.join(row))
print("\nTotal no. of rows: %d"%(data.line_num))
print('Field names are:')
print(', '.join(field for field in fields))

