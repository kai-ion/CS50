from pyfiglet import Figlet
import sys
import random

def main() :
    figlet = Figlet()
    figlet.getFonts()

    if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") :
        try :
            figlet.setFont(font= sys.argv[2])
            ...

        except :
            sys.exit("Invalid Usage")
    elif len(sys.argv) == 1 :
        fonts = random.choice(figlet.getFonts())
        figlet.setFont(font = fonts)
        ...
    ...

    msg = input("Input: ")

    print("Output: ")

    print(figlet.renderText(msg))

if __name__ == "__main__" :
    main()