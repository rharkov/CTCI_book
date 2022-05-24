import pytest


def palindrome_permutation(phrase):
    """checks if a string is a permutation of a palindrome"""
    table = [0 for _ in range(ord("z") - ord("a") + 1)]
    countodd = 0
    for c in phrase:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2:
                countodd += 1
            else:
                countodd -= 1

    return countodd <= 1


def char_number(c):
    a = ord("a")
    z = ord("z")
    upper_a = ord("A")
    upper_z = ord("Z")
    val = ord(c)

    if a <= val <= z:
        return val - a

    if upper_a <= val <= upper_z:
        return val - upper_a
    return -1


# class Test(.TestCase):
#     test_cases = [
#         ("aba", True),
#         ("aab", True),
#         ("abba", True),
#         ("aabb", True),
#         ("a-bba", True),
#         ("a-bba!", True),
#         ("Tact Coa", True),
#         ("jhsabckuj ahjsbckj", True),
#         ("Able was I ere I saw Elba", True),
#         ("So patient a nurse to nurse a patient so", False),
#         ("Random Words", False),
#         ("Not a Palindrome", False),
#         ("no x in nixon", True),
#         ("azAZ", True)
#     ]
#
#     def test_pal_perm(self):
#         for [value, expected] in self.test_cases:
#             with self.subTest(value=value):
#                 self.assertEqual(palindrome_permutation(value), expected)
#
#
# if __name__ == "__main__":
#     unittest.main()

# print(palindome_permutation("Tact Coa"))
@pytest.mark.parametrize("value,expected", [
    ("aba", True),
    ("aab", True),
    ("abba", True),
    ("aabb", True),
    ("a-bba", True),
    ("a-bba!", True),
    ("Tact Coa", True),
    ("jhsabckuj ahjsbckj", True),
    ("Able was I ere I saw Elba", True),
    ("So patient a nurse to nurse a patient so", False),
    ("Random Words", False),
    ("Not a Palindrome", False),
    ("no x in nixon", True),
    ("azAZ", True)
])


def test_palindrome_permutation(value, expected):
    assert palindrome_permutation(value) == expected


