#Import Data
import csv
with open('contactinfo.csv', newline='') as csvfile:
  contacts = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in contacts:
    print(', '.join(row))
#Import Data
import csv
with open('personinfo.csv', newline='') as csvfile:
  persons = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in persons:
    print(', '.join(row))
