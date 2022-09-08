from fuel import convert,gauge


def main () :
    test_input()
    ...

def test_input() :
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("1/100") == 1 and gauge(25) == "E"
    assert convert("99/100") == 1 and gauge(25) == "F"

if __name__ == "__main__" :
    main()