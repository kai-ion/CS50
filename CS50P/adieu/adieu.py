import inflect

def main() :
    output = "Liesl"
    while True:
        try :
            name = input("Name: ")
            output = inflect.join(name)
        except EOFError:
            print()
            break

    print(f"Adieu, adieu, to {output}")

    ...

if __name__ == "__main__" :
    main()