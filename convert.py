def roman_to_int(self, s: str) -> int:
    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    total = 0
    for i in range(len(s)):
        if i != 0 and roman_numerals[s[i - 1]] < roman_numerals[s[i]]:
            total -= roman_numerals[s[i - 1]] * 2
        total += roman_numerals[s[i]]
    return total
