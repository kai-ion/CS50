import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s) :
        if int(match.group(1)) > 12 or int(match.group(5)) > 12 :
            raise ValueError
        return match.groups()
    else :
        return ValueError
        ...
    ...


...


if __name__ == "__main__":
    main()