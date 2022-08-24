import inflect

p = inflect.engine()

def main() :
    nameList = ["Liesl"]
    while True:
        try :
            name = input("Name: ")

            output = p.join(nameList)

        except EOFError:
            print()
            nameList.append(name)
            break

    print(f"Adieu, adieu, to {output}")

    ...

if __name__ == "__main__" :
    main()