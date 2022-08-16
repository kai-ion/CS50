grocery = {

}

def main() :
    get_int("")

    ...
def get_int(prompt) :
    while True:
        try:
            item = input(prompt).capita
            if item in grocery :
                grocery[item] = grocery[item] + 1
            else :
                grocery[item] = 1

        except (EOFError):
            print()
            print(grocery)
            break


if __name__ == "__main__" :
    main()
    ...