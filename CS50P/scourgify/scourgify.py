import sys
import csv
import tabulate

output = []

def main() :
    check_command_line_arg()

    try :
        with open(sys.argv[1], "r") as table:
            reader = csv.DictReader(table)
            for row in reader :
                nameSplit = row["name"].split(",")
                output.append({"firstName" : nameSplit[1], "lastName" : nameSplit[0], "house" : row["house"]})

        for student in sorted(output, key=lambda student: student["lastName"]):
            print(f"{student['lastName']} {student['firstName']}is in {student['house']}")
        ...
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["first name", "last name", "house"])
        for name in sor
    ...


def check_command_line_arg() :
    if len(sys.argv) < 3 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3 :
        sys.exit("Too many command-line arguments")

    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

if __name__ == "__main__" :
    main()