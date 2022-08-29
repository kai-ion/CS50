```def main () :
    str = input("Input: ")

    for i in str :

        if i.upper() in ['A', 'E', 'I', 'O', 'U'] :
            print('', end="")

        else :
            print(i, end="")
    print()

main()```