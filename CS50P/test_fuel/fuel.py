def main() :
    '''
    num = get_int("Fraction: ")
    newNum = round(num * 100)

    if newNum <= 1 :
        print("E")
    elif newNum >= 99:
        print("F")
    else :
        print(f"{newNum}%")
    ...
'''
    num = input("Fraction: ")

    numConverted = convert(num)
    output = gauge(numConverted)
    print(output)


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

def convert(fraction):
    while True:
        try:
            numerator, denominator = fraction.split("/")
            newNum = int(numerator)
            newDen = int (denominator)
            fuel = newNum / newDen
            if fuel <= 1:
                fuelConverted = int(fuel * 100)
                return fuelConverted
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            pass
    ...


def gauge(percentage):
    if percentage <= 1 :
        return "E"
    elif percentage >= 99:
        return "F"
    else :
        return str(percentage) + "%"
    ...

if __name__ == "__main__" :
    main()