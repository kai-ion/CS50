import numb3rs

def main() :
    test_format()
    test_range()
    ...

def test_format() :
    assert numb3rs.validate("1.2.3.4") == True
    assert numb3rs.validate("1.2.3.") == False

    ...

def test_range() :
    ...

if __name__ == "__main__" :
    main()