from pyfiglet import Figlet
import sys

def main() :
    figlet = Figlet()
    figlet.getFonts()

    if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") :
        try :
            ...

        except :
            ...
    ...

if __name__ == "__main__" :
    main()