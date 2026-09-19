import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "grade"])
    writer.writerow(["Rie", 20, 88])
    writer.writerow(["Won", 22, 91])
    writer.writerow(["Rina", 26, 95])

# read the csv files
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)