import twttr

def main() :
    test_cases()
    ...

def test_cases() :
    assert twttr.shorten("twitter") == "twttr"
    assert twttr.shorten("TWITTER") == "TWTTR"
    assert twttr.shorten("TwItTeR") == "TwtTR"

def test_number() :
    assert twttr.shorten("1234") == "1234"

def test_punctuation() :
    assert twttr.shorten("?!.,") == "?!.,"

if __name__ == "__main__" :
    main()