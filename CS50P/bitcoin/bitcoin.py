import sys
import requests

def main() :

    if sys.argv < 2 :
        sys.exit("Missing command-line argument")


    try:
        n = float(sys.argv[2])
        ...
    except requests.RequestException:
        ...
    ...

if __name__ == "__main__" :
    main()