from plates import is_valid

def main() :
    is_valid_length()
    is_valid_start()
    ...

def is_valid_length() :
    assert is_valid("AA") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False

def is_valid_start() :
    assert is_valid("AA") == True
    assert is_valid("1A") == False
    assert is_valid("A1") == False

if __name__ == "__main__":
    main()