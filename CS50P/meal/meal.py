def main():
    str = input("What time is it? ")

    time = convert(str)

    if time >= 7 or time <=8 :
        print("breakfast time")
    elif time >= 7 or time <=8 :
        print("lunch time")
    elif time >= 7 or time <=8 :
        print("dinner time")
    ...


def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes) / 60
    return int(hours) + minutes


if __name__ == "__main__":
    main()