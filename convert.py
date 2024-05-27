"""Convert a roman numeral string to an integer"""

from itertools import chain, pairwise

ROMAN_NUMERALS = {
    "": 0,
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def using_itertools(roman: str) -> int:
    """Convert a roman numeral string to an integer"""
    total = 0
    for prev, curr in chain({("", roman[0])}, pairwise(roman)):
        if ROMAN_NUMERALS[prev] < ROMAN_NUMERALS[curr]:
            total -= ROMAN_NUMERALS[prev] * 2
        total += ROMAN_NUMERALS[curr]
    return total


def using_rangelen(roman: str) -> int:
    """Convert a roman numeral string to an integer"""
    total = 0
    for i in range(len(roman)):
        prev = roman[i - 1]
        curr = roman[i]
        if i != 0 and ROMAN_NUMERALS[prev] < ROMAN_NUMERALS[curr]:
            total -= ROMAN_NUMERALS[prev] * 2
        total += ROMAN_NUMERALS[curr]
    return total


def using_enumerate(roman: str) -> int:
    """Convert a roman numeral string to an integer"""
    total = 0
    for i, _ in enumerate(roman):
        if i != 0 and ROMAN_NUMERALS[roman[i - 1]] < ROMAN_NUMERALS[roman[i]]:
            total -= ROMAN_NUMERALS[roman[i - 1]] * 2
        total += ROMAN_NUMERALS[roman[i]]
    return total


assert using_enumerate("III") == 3
assert using_enumerate("XIV") == 14
assert using_enumerate("XCVII") == 97
assert using_enumerate("MCMLXXVI") == 1976
print("all tests passed!")
