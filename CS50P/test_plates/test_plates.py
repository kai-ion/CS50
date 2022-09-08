from plates import is_valid

def main() :

    test_length()
    test_start()
    test_number()
    test_0()
    test_punctuation()


def test_length() :
    assert is_valid("AA") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False

def test_start() :
    assert is_valid("AA") == True
    assert is_valid("1A") == False
    assert is_valid("A1") == False

def test_number() :
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_0() :
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_punctuation() :
    assert is_valid("CS.50") == False
    assert is_valid("CS!05") == False
    assert is_valid("CS 05") == False

if __name__ == "__main__" :
    main()