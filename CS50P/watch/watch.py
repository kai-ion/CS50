import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s) :
        if match := re.search(r"(http(s)?:\/\/(www\.)?youtube\.com\/embed\/)([a-z_A-Z_0-9_]+)", s, re.IGNORECASE) :
            url = match.group(4)

            return "https://youtu.be/" + url
    ...


...


if __name__ == "__main__":
    main()