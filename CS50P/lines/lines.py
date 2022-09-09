import sys

def main() :

    check_command_line_arg()

    try :
        with open(sys.argv[1], "r") as file :
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    ...

def check_command_line_arg() :
    if len(sys.argv) < 2 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2 :
        sys.exit("Too many command-line arguments")

    if ".py" not in sys.argv[1] :
        sys.exit("Not a Python file")
    ...

if __name__ == "__main__" :
    main()