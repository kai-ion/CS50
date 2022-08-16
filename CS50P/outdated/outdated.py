month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main() :
    get_int("")

def get_int(prompt) :
    while True:
        date = input(prompt).lower()
        try:
            year, months, day = date.split("/")
            if int(months) >= 1 and int(months) <= 12 and int(day) >= 1 and int(day) <= 31:
                print(f"{year}-{months}-{day}")

        except:
            print()
            break

if __name__ == "__main__" :
    main()
    ...