grocery = {

}

def main() :
    get_int("")

    ...
def get_int(prompt) :
    while True:
        try:
            item = input(prompt).lower()
            if item in grocery :
                grocery[item] = grocery[item] + 1
            else :
                grocery[item] = 1

        except (EOFError):
            print()

            for items in sorted(grocery.keys()) :
                print(grocery[items], items.upper())
            break


if __name__ == "__main__" :
    main()
    ...