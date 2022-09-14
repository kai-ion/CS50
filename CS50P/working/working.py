import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"/^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$/gm", s, re.IGNORECASE) :
        return match.groups()
    else :
        return ValueError
        ...
    ...


...


if __name__ == "__main__":
    main()