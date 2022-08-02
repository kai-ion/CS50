def main() :
    str = input("Greeting: ").strip()

    if str == "Hello" :
        print("$0")
    elif str[0] == 'h' :
        print("$20")
    else :
        print("$100")

main()