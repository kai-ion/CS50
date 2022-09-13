import numb3rs

def main() :
    test_format()
    test_range()
    ...

def test_format() :
    assert numb3rs.validate(r"1.2.3.4") == True
    assert numb3rs.validate(r"1.2.3.") == False
    assert numb3rs.validate(r"cat") == False


    ...

def test_range() :
    assert numb3rs.validate(r"1.2.3.255") == True
    assert numb3rs.validate(r"1.2.3.1000") == False

    ...

if __name__ == "__main__" :
    main()