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
    roman_dict = {"I": 1, "II": 2, "III": 3, "IV": 4,
                  "V": 5, "VI": 6, "VII": 7, "VIII": 8}
    return roman_dict[roman]
