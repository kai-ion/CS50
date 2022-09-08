def main() :
    str = input("Greeting: ")

    greeting = value(str)

    print(f"${greeting}")

def value(greeting) :

    greeting = greeting.strip().lower()

    if "hello" in greeting :
        return int(0)
    elif greeting[0] == 'h' :
        return int(20)
    else :
        return int(100)

if __name__ == "__main__" :
    main()