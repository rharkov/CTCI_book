# def URLify(string, strLen):
#     splitStr = list(string)
#     for idx, char in enumerate(splitStr):
#         if char == " ":
#             splitStr[idx] = "%20"
#     return ''.join(splitStr)

def URLify(string, length):
    return string[:length].replace(' ','%20')

print(URLify("Mr John Smith                         ", 13))
