months = [
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
            month, day, year = date.split("/")
            if int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
                break
        except:
            try:
                month2, day2, year = date.split(" ")

                for i in range(len(months)) :
                    if month2 == months[i] :
                        month = i

                day = day2.replace("," , "")
                
                if int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
                    break
            except:
                pass
    print(f"{year}-{int(month):02}-{int(day):02}")

if __name__ == "__main__" :
    main()
    ...