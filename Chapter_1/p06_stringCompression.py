import pytest

def stringCompression(string):
    resultStr = ''
    tempCount = 0
    prevLetter = ''

    for letter in string:
        if not prevLetter:
            prevLetter = letter
            tempCount += 1
        elif prevLetter != letter:
            resultStr += prevLetter + str(tempCount)
            prevLetter = letter
            tempCount = 1
        else:
            tempCount += 1
    resultStr += prevLetter + str(tempCount)
    return string if string == resultStr else resultStr

@pytest.mark.parametrize("value,expected", [
    ("aaabbccc","a3b2c3"),
    ("hrqe","h1r1q1e1"),
    ("uuuuu","u5")
])

def test_stringCompression(value, expected):
    print(stringCompression(value))
    assert stringCompression(value) == expected
