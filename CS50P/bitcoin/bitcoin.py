import sys
import requests

def main() :

    if sys.argv < 2 :
        sys.exit("Missing command-line argument")
    try:
        ...
    except requests.RequestException:
        ...
    ...

if __name__ == "__main__" :
    main()