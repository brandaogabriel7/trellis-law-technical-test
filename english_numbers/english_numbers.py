numbers_in_english = {
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


def hundred(number: int) -> str:
    return f"{numbers_in_english[number]} hundred"


def english_number(number: int) -> str:
    if number <= 99:
        return english_number_below_one_hundred(number)

    hundreds = number // 100
    rest = number - hundreds * 100

    if rest == 0:
        return hundred(hundreds)

    return f"{hundred(hundreds)} and {english_number_below_one_hundred(rest)}"


def english_number_below_one_hundred(number):
    if number == 0:
        return "zero"

    if number in numbers_in_english:
        return numbers_in_english[number]

    if number in tens_in_english:
        return tens_in_english[number]

    tens = number // 10
    units = number - tens * 10
    return f"{tens_in_english[tens * 10]}-{numbers_in_english[units]}"
