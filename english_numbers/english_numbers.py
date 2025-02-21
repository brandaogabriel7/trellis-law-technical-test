numbers_in_english = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

tens_in_english = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}


def write_number_in_english(number: int) -> str:
    if number > 19:
        tens = number // 10 * 10
        units = number % 10
        if units:
            return f"{tens_in_english[tens]}-{numbers_in_english[units]}"
        else:
            return tens_in_english[tens]
    else:
        return numbers_in_english[number]
