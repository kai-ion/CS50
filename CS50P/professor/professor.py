import random


def main():
    lvl = get_level()

    x = generate_integer(lvl)
    y = generate_integer(lvl)
    ...


def get_level():
    while True :
        try :
            num = int(input("Level: "))

            if num in [1,2,3] :
                return num
            ...
        except ValueError :
            pass
    ...


def generate_integer(level):
    if level == 1 :
        return random.randint(0, 9)
    elif level == 2 :
        return random.randint(10, 99)
    elif level == 3 :
        return random.randint(100, 999)
    ...


if __name__ == "__main__":
    main()

