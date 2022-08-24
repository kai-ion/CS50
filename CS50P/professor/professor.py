import random


def main():
    lvl = get_level()
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
    ...


if __name__ == "__main__":
    main()

