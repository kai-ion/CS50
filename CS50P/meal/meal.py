def main():
    str = input("What time is it? ")

    time = convert(str)
    ...


def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes) / 60
    return int(hours) + minutes


if __name__ == "__main__":
    main()