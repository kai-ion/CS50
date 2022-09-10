def main() :
    check_command_line_arg()
    ...


def check_command_line_arg() :
    if len(sys.argv) < 3 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3 :
        sys.exit("Too many command-line arguments")

    if ".py" not in sys.argv[1] :
        sys.exit("Not a Python file")

if __name__ == "__main__" :
    main()