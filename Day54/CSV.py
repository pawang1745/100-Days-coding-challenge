#Comma-Separated Values
#Opening A CSV File

import csv

with open("January.csv") as file:
  reader = csv.reader(file)
  line = 0

  for row in reader:
    print (row)

#Make it Beautiful!
import csv

with open("January.csv") as file:
  reader = csv.reader(file)
  line = 0

  for row in reader:
    print (", ".join(row))

#Filter the Output
import csv

with open("January.csv") as file:
  reader = csv.DictReader(file)
  line = 0
  for row in reader: 
    print (row["Net Total"])

import csv
with open("January.csv") as file:
  reader = csv.DictReader(file)
  total = 0
  for row in reader:
    print (row["Net Total"])
    total += float(row["Net Total"])

print(f"Total: {total}") 

#day54 challenge
import csv

total = 0.0

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    total += float(row["Quantity"]) * float(row["Cost"])

print(f"Total: ${round(total,2)}")
