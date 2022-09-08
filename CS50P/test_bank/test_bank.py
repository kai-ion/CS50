import bank

def main() :
    test_return_0()
    ...

def test_return_0():
    assert bank.value("hello") == 0
    assert bank.value("Hello") == 0
    assert bank.value("Hello, world") == 0
    ...

def test_return_20():
    ...

def test_return_100():
    ...

if __name__ == "__main__" :
    main()