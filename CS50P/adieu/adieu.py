import inflect

p = inflect.engine()

def main() :
    nameList = []
    while True:
        try :
            name = input("Name: ")
            nameList.append(name)


        except EOFError:
            print()
            output = p.join(nameList)
            break

    print(f"Adieu, adieu, to {output}")

    ...

if __name__ == "__main__" :
    main()