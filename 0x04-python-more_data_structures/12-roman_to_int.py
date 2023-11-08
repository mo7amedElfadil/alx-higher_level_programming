#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    su = 0
    for c in range(len(roman_string)):
        try:
            su += (roman[roman_string[c]],
                   -roman[roman_string[c]])[roman[roman_string[c + 1]]
                                            > roman[roman_string[c]]]
        except IndexError:
            su += roman[roman_string[c]]
    return (su)
