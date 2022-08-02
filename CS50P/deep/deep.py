def main() :
    str = input("What is the answer to the Great Question of Life, the Universe and Everything ").lower().strip()

    if str == "42" or str == "forty-two" or str == "forty two":
        print("yes")
    else :
        print("no")
main()