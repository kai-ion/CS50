def main() :
    get_int("Item: ")

    ...
def get_int(prompt) :
    total = 0
    while True:
        try:
            item = input(prompt).title()
            if item in menu :
                total += menu[item]

                print(f"Total: ${total:.2f}")
        except (EOFError):
            print()
            break


if __name__ == "__main__" :
    main()
    ...