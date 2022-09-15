from validator_collection import validators, checkers, errors

def main() :
    mail = validate(input("What's your email address? "))

    print(mail)
    ...

def validate(s) :
    try:
        email_address = validators.email(s)
        # Will raise an EmptyValueError
    except errors.EmptyValueError:
        # Handling logic goes here
        return "Invalid"

    except errors.InvalidEmailError:
        # More handlign logic goes here
        return "Invalid"

    return "Valid"

    ...

if __name__ == "__main__" :
    main()