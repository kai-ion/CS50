grocery = {

}

def main() :
    get_int("")

    ...
def get_int(prompt) :
    total = 0
    while True:
        try:
            item = input(prompt)
            if item in grocery :
                grocery[item] = grocery[item] + 1
            else :
                grocery[item] = 1

                print(f"Total: ${total:.2f}")
        except (EOFError):
            print()
            break


if __name__ == "__main__" :
    main()
    ...