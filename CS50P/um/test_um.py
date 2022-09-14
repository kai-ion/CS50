import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(r"\b\W*um\W", s)
    return len(s)
    ...


...


if __name__ == "__main__":
    main()