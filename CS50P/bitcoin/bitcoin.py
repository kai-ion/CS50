import sys
import requests

def main() :

    if sys.argv < 2 :
        sys.exit("Missing command-line argument")


    try:
        n = float(sys.argv[2])
        ...
    except (requests.RequestException or ValueError):
        if ValueError :
            sys.exit("Command-line argument is not a number")
        else :
            sys.exit("Request Error")
        ...
    ...

if __name__ == "__main__" :
    main()