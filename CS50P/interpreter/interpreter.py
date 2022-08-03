def main() :
    str = input("Expression: ")
    x, y, z = str.split(" ")

    if '+' in y :
        print(float(x) + float(z))
    elif '-' in y :
        print(float(x) - float(z))
    elif '*' in y :
        print(float(x) * float(z))
main()