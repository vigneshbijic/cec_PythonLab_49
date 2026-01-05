import csv

filepath = input("Enter CSV file path: ")

try:
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            print(row)    # each row is already a list of strings

except FileNotFoundError:
    print("Error: File not found!")

except Exception as e:
    print("An error occurred:", e)
