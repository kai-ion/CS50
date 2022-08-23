import emoji

def main() :
    str = input("Input: ")

    output = emoji.emojize(str)

    print(f"Output: {output}")

    ...

if __name__ == "__main__" :
    main()