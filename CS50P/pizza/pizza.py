import sys
import tabulate

def main() :
    check_command_line_arg()

    with open(sys.argv[1]) as table:
        print(tabulate.tabulate(table, headers = "firstrow"))
    ...

def check_command_line_arg() :
    if len(sys.argv) < 2 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2 :
        sys.exit("Too many command-line arguments")

    if ".csv" not in sys.argv[1] :
        sys.exit("Not a Python file")

if __name__ == "__main__" :
    main()