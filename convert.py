"""Convert a roman numeral string to an integer"""

ROMAN_NUMERALS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def roman_to_int(roman: str) -> int:
    """Convert a roman numeral string to an integer"""
    total = 0
    for i, _ in enumerate(roman):
        if i != 0 and ROMAN_NUMERALS[roman[i - 1]] < ROMAN_NUMERALS[roman[i]]:
            total -= ROMAN_NUMERALS[roman[i - 1]] * 2
        total += ROMAN_NUMERALS[roman[i]]
    return total


assert roman_to_int("III") == 3
assert roman_to_int("XIV") == 14
assert roman_to_int("XCVII") == 97
assert roman_to_int("MCMLXXVI") == 1976
print("all tests passed!")
