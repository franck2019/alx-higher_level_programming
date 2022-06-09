#!/usr/bin/python3

def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}

    rs = roman_string.upper()
    number = 0
    length = len(rs)

    i = 0
    while i < length:
        if rs[i] in roman_dict:
            if i + 1 < length:
                if rs[i] in 'I' and rs[i + 1] in ['V', 'X']:
                    number += roman_dict[rs[i + 1]] - 1
                    i += 2
                elif rs[i] in 'X' and rs[i + 1] in ['L', 'C']:
                    number += roman_dict[rs[i + 1]] - 10
                    i += 2
                elif rs[i] in 'C' and rs[i + 1] in ['D', 'M']:
                    number += roman_dict[rs[i + 1]] - 100
                    i += 2
                else:
                    number += roman_dict[rs[i]]
                    i += 1
            else:
                number += roman_dict[rs[i]]
                i += 1

    return number
