import twttr

def main() :
    ...

def test_cases() :
    assert twttr.shorten("twitter") == "twttr"
    assert twttr.shorten("T") == "twttr"

if __name__ == "__main__" :
    main()