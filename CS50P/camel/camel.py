def main () :
    str = input("camelCase: ")

    print("snake_case: ", end="")

    for letter in str :
        if letter.isupper():
            print("_" + letter.lower(), end="")
        else :
            print(letter, end="")
    print()
    ...
main()