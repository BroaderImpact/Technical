import csv
with open('CtG.csv', newline='') as csvfile:
  volunteers = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in volunteers:
    print(', '.join(row))
