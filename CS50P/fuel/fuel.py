def main() :
    num = get_int("Fraction: ")
    newNum = num * 100

    if newNum <= 1 :
        print("E")
    elif newNum >= 99:
        print("F")
    else :
        print(f"{newNum}%")
    ...

def get_int(prompt) :
    while True:
        try:
            fuel = input(prompt)
            numerator, denominator = fuel.split("/")
            newNum = int(numerator)
            newDen = int (denominator)
            f = newNum / newDen
            if f <= 1:
                return f
        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__" :
    main()