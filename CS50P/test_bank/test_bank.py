import bank

def main() :
    test_return_0()
    test_return_20()
    test_return_100()
    ...

def test_return_0():
    assert bank.value('hello') == 0
    assert bank.value("Hello") == 0
    assert bank.value("Hello, world") == 0
    ...

def test_return_20():
    assert bank.value('hi') == 20
    assert bank.value("Hey") == 20
    ...

def test_return_100():
    ...

if __name__ == "__main__" :
    main()