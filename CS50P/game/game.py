import random
def main() :
    while True:
        try :
            num = int(input("Level: "))

            if (num < 1):
                continue

            randNum = random.randint(1, num)
            guess = int(input("Guess: "))

            if guess < 1 :
                continue
            
        except ValueError:
            pass

    ...

if __name__ == "__main__" :
    main()