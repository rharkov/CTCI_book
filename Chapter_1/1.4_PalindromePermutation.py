def palindome_permutation(string):
    # checks if a string is a permutation of a palindrome
    table = [0 for _ in range(ord('z') - ord('a')+1)]
    print(table)


def char_number(char):
    a = ord('a')
    z = ord('z')
    upper_a = ord("A")
    upper_z = ord('Z')
    val = ord(char)

    if a <= val <= z:
        return val - a
    if upper_a <= val <= upper_z:
        return val - upper_a
    return -1


palindome_permutation("Tact Coa")
