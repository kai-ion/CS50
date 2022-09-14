from working import convert
import pytest

def main() :
    test_format()
    test_time()
    test_hour()
    test_minute()
    ...

def test_format() :
    with pytest.raises(ValueError) :
        convert('9 AM - 9 PM')
    ...

def test_time() :
    ...

def test_hour() :
    ...

def test_minute() :
    ...

if __name__ == "__main__" :
    main()