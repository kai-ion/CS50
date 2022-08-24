import inflect

def main() :
    try :
        name = input("Name: ")
        output = inflect.join(name)
    ...

if __name__ == "__main__" :
    main()