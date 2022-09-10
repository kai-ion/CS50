import sys
import csv
import tabulate

def main() :
    check_command_line_arg()

    try :
        with open(sys.argv[1], "r") as table:
            reader = csv.reader(table)
            for row in table :
                name, house = reader
                print(row)

        ...
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
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