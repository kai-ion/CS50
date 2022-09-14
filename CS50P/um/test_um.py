from um import count


def main():
    test_upperCase()
    test_word()
    test_space()

def test_upperCase() :
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    ...

def test_word() :
    assert count("yuummi") == 0
    ...

def test_space() :
    assert count("um?") == 1
    assert count("hi um okay") == 1
    ...



if __name__ == "__main__":
    main()