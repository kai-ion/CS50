def main() :
    str = input("Greeting: ").strip().lower()

    output = value(str)

    print(f"${output}")

def value(greeting) :
    if "hello" in str :
        return 0
    elif greeting[0] == 'h' :
        return 20
    else :
        return 100

main()