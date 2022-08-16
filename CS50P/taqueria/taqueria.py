menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main() :
    num = get_int("Item: ")
    newNum = round(num * 100)

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
            item = input(prompt).title()
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