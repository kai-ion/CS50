def convert(str):
    return str.replace(":)", "🙂").replace(":(","😐")

def main() :
    str = input("Enter a phrase: ")

    print(convert(str))

main()