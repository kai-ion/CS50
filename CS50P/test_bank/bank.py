def main() :
    str = input("Greeting: ")

    output = value(str)

    print(f"${output}")

def value(greeting) :

    greeting = greeting.strip().lower()
    if "hello" in greeting :
        return 0
    elif greeting[0] == 'h' :
        return 20
    else :
        return 100

main()