def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6 :
        return False

    #if s[0].isalpha() == False or s[1].isalpha() == False:
    #    return False
    if s[:2].isalpha() == False:
        return False

    for i in s :
        if i.isdigit() :
            index = s.index(i)
            if s[index:].isdigit() == False:
                return False

    i = 0
    while i < len(s) :
        if s[i].isdigit() :
            if s[i] == '0':
                return False
            else :
                break
        i += 1


    for letter in s :
        if letter in ['.', ' ', '?', '!'] :
            return False
    #if plate.isalnum() :
    #   return False

    return True
    
if __name__ == "__main__":
    main()