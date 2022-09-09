import sys

def main() :
    if len(sys.argv) < 2 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2 :
        sys.exit("Too many command-line arguments")

    if ".py" not in sys.argv[1] :
        sys.exit("Not a Python file")

    try :
        with open(sys.argv[1], "r") as file :
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    ...

if __name__ == "__main__" :
    main()