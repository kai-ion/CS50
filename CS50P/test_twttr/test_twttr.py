import twttr

def main() :
    ...

def test_cases() :
    assert twttr.shorten("twitter") == "twttr"
    assert twttr.shorten("TWITTER") == "TWTTR"
    assert twttr.shorten("TwItTeR") == "TwtTR"

if __name__ == "__main__" :
    main()