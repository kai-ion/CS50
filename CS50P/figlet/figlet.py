from pyfiglet import Figlet
import sys

def main() :
    figlet = Figlet()
    figlet.getFonts()

    if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") :
        try :
            figlet.setFont(font= sys.argv[2])
            ...

        except :
            sys.exit("Invalid Usage")
            ...
    ...

if __name__ == "__main__" :
    main()