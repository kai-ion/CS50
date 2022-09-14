import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"", s, re.IGNORECASE) :
        return match.groups()
    else :
        return ValueError
        ...
    ...


...


if __name__ == "__main__":
    main()