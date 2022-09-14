import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s) :
 #       if int(match.group(1)) > 12 or int(match.group(5)) > 12 :
   #         raise ValueError
        start = time_format(match.group(1), match.group(2), match.group(3))
        end = time_format(match.group(5), match.group(6), match.group(7))
        return start + 'to' + end
    else :
        return ValueError
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
            new_hour = 0
        else:
            new_hour = int(hour)

    if minute == None:
        newMinute = ':00'
        newTime = newHour + newMinute
    else:
        newTime = newHour + ":" + minute

    return newTime

if __name__ == "__main__":
    main()