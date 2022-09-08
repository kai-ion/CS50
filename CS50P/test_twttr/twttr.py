'''def main () :
    str = input("Input: ")

    for i in str :

        if i.upper() in ['A', 'E', 'I', 'O', 'U'] :
            print('', end="")

        else :
            print(i, end="")
    print()

main()
'''

def main() :
    str = input("Input: ")

    word = shorten(str)

    print(f"Output: {word}")
    ...


def shorten(word):
    str = ""
    for i in word :

        if not i.upper() in ['A', 'E', 'I', 'O', 'U'] :
            str += i

    return str
    ...

if __name__ == "__main__":
    main()