def add_numbers(a: int, b: int):
    return a + b

def palindrom(word :str):
     return str(word).lower() == str(word)[::-1].lower()

def test_is_polindrom():
    word ="aabbaa"
    expected = True
    assert palindrom(word) == expected

def test_is_polindrom_uper():
    word = "AABBAA"
    expected = True
    assert palindrom(word) == expected

def test_polindrom_is_empty():
    word = ""
    expected = True
    assert palindrom(word) == expected

def test_polindrom_is_number():
    word = "a1bb1a"
    expected = True
    assert palindrom(word) == expected

def test_palindrom_is_int():
      assert palindrom(121)

