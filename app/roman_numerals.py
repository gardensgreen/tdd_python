# def parse(roman):
#     if roman == "I":
#         return 1
#     elif roman == "II":
#         return 2
#     elif roman == "III":
#         return 3
#     elif roman == "IV":
#         return 4
#     elif roman == "V":
#         return 5
#     elif roman == "VI":
#         return 6
#     elif roman == "VII":
#         return 7
#     else:
#         return 8


def parse(roman):
    # roman_dict = {"I": 1, "II": 2, "III": 3, "IV": 4,
    #               "V": 5, "VI": 6, "VII": 7, "VIII": 8, 'IX': 9, "X": 10}

    # return roman_dict[roman]
    roman_dict = {"I": 1, "V": 5, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}

    num = 0
    char_array = list(roman)
    for i in range(len(char_array) - 1):
        if (roman_dict[char_array[i]] < roman_dict[char_array[i+1]]):
            num -= roman_dict[char_array[i]]

        else:
            num += roman_dict[char_array[i]]
    num += roman_dict[char_array[len(char_array) - 1]]
    return num


print(parse("XI"))
print(parse("XIV"))
print(parse("XIX"))
print(parse("XX"))
print(parse("XXXIV"))
print(parse("XLI"))
print(parse("L"))
print(parse("XCIX"))
print(parse("C"))
print(parse("CCCXXXIII"))
print(parse("DLV"))
print(parse("CDXLIX"))
print(parse("MCMLXXII"))
