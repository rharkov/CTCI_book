def stringRotation(str1,str2):
    if (len(str1) == len(str2)) != 0:
        return str2 in str1*2
    return False


print(stringRotation('waterbottle', 'erbottlewat'))
