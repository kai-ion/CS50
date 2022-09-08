def main() :
    str = input("Greeting: ")

    output = value(str)

    print(f"${output}")

def value(greeting) :

    greeting = greeting.strip().lower()

    if "hello" in greeting :
        return int(0)
    elif greeting[0] == 'h' :
        return int(20)
    else :
        return int(100)

main()