import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = "([0-9][0-2]*):*([0-5][0-9])* ([A-P]M)"
    if match := re.search(r"^" + regex + " to " + regex + "$", s) :
        strs = match.groups()
        if int(match.group(1)) > 12 or int(match.group(5)) > 12 :
            raise ValueError

        start = time_format(match.group(1), match.group(2), match.group(3))
        end = time_format(match.group(4), match.group(5), match.group(6))
        return start + ' to ' + end
    else :
        raise ValueError
        ...
    ...


def time_format(hour, minute, amPM) :
    if amPM == 'PM' :
        if int(hour) == 12:
            newHour = 12
        else :
            newHour = int(hour) + 12
    else :
        if int(hour) == 12:
            newHour = 0
        else:
            newHour = int(hour)

    if minute == None:
        newMinute = ':00'
        newTime = f"{newHour:02}" + newMinute
    else:
        newTime = f"{newHour:02}" + ":" + minute

    return newTime

if __name__ == "__main__":
    main()