import inflect

p = inflect.engine()

def main() :
    namesList = 
    while True:
        try :
            name = input("Name: ")
            output = p.join(name)

            nameList.append(name)

        except EOFError:
            print()
            break

    print(f"Adieu, adieu, to {output}")

    ...

if __name__ == "__main__" :
    main()