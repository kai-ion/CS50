import sys
import requests
import json

def main() :

    if len(sys.argv) < 2 :
        sys.exit("Missing command-line argument")


    try:
        n = float(sys.argv[1])
        ...
    except ValueError:
        sys.exit("Command-line argument is not a number")
        ...

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        #print(json.dumps(response.json(), indent=2))
        rate = response["bpi"]["USD"]["rate"]
        print(float(rate))
        ...
    except requests.RequestException:
        sys.exit("Request Error")
        ...
    ...

if __name__ == "__main__" :
    main()