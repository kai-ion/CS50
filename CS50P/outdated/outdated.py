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
        try:
            date = input(prompt).lower()
            year, months, day = date.split("/")
            print(f"{year}, {months}, {day}")

        except (EOFError):
            print()
            break

if __name__ == "__main__" :
    main()
    ...