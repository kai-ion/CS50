import sys

def main() :
    check_command_line_arg()

    try :
        ...
    except FileNotFoundError:
        sys.exit(f"could not read {sys.argv[1]}")
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