fruits = {
    "apple" : 130,
    "avocado" : 50,
    "kiwifruit" : 90,
    "pear" : 100,
    "sweet cherries" : 100,
}

def main() :

    str = input("Item: ").lower()

    if str in fruits :
        print("calories:", fruits[str])
    ...
main()