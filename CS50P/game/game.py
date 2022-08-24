import random
import sys

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

            if guess < randNum :
                print("Too small!")
                continue
            elif guess > randNum :
                print("Too large!")
                continue
            else :
                sys.exit("Just right!")

        except ValueError:
            pass



    ...

if __name__ == "__main__" :
    main()