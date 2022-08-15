def main() :
    num = get_int("Fraction: ")

    ...

def get_int(prompt) :
    while True:
        try:
            return int(input(prompt))
        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__" :
    main()