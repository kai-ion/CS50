import random


def main():
    lvl = get_level()

    score = 0
    for i in range(10) :

        for i in range(10) :
            try :
                x = generate_integer(lvl)
                y = generate_integer(lvl)

                counter = 0
                while counter < 3 :
                    ans = (f"{x} + {y} = ")
                    if int(ans) != x + y :
                        print("EEE")
                        counter += 1
                    elif int(ans) == x + y :
                        print(f"{x} + {y} = {x + y}")
                        score += 1
                        break


            except ValueError:
                pass
    print(f"Score: {score}")
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

