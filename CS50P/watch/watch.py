import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"",s) :
        if match := re.search(r"", s) :
            url = match.group(3)

            return "https://youtu.be/" + url
    ...


...


if __name__ == "__main__":
    main()