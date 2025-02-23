NUMBERS_IN_ENGLISH = {
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

TENS_IN_ENGLISH = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

ORDERS_OF_MAGNITUDE_IN_ENGLISH = {
    0: "",
    1: "thousand",
    2: "million",
    3: "billion",
    4: "trillion",
}

MAX_NUMBER = 999999999999999


def get_english_number(number: int) -> str:
    if number > MAX_NUMBER:
        raise ValueError("Number is too large")

    if number < 1000:
        return __get_english_number_below_one_thousand(number)

    current_number = number
    number_groups_stack = []

    while current_number > 0:
        number_groups_stack.append(current_number % 1000)
        current_number = current_number // 1000

    number_groups_stack.append(current_number)

    result = ""
    while len(number_groups_stack) > 0:
        number_group = number_groups_stack.pop()
        order_of_magnitude = len(number_groups_stack)
        if number_group == 0:
            continue

        if result != "":
            result += " "

        result += f"{__get_english_number_below_one_thousand(number_group)} {ORDERS_OF_MAGNITUDE_IN_ENGLISH[order_of_magnitude]}".strip(
        )

    return result.strip()


def __get_english_number_below_one_thousand(number: int) -> str:
    if number <= 99:
        return __get_english_number_below_one_hundred(number)

    hundreds = number // 100
    rest = number % 100

    if rest == 0:
        return f"{NUMBERS_IN_ENGLISH[hundreds]} hundred"

    return f"{NUMBERS_IN_ENGLISH[hundreds]} hundred and {__get_english_number_below_one_hundred(rest)}"


def __get_english_number_below_one_hundred(number: int) -> str:
    if number < 0:
        raise ValueError("Number must be positive")

    if number == 0:
        return "zero"

    if number in NUMBERS_IN_ENGLISH:
        return NUMBERS_IN_ENGLISH[number]

    if number in TENS_IN_ENGLISH:
        return TENS_IN_ENGLISH[number]

    tens = number // 10
    units = number % 10

    return f"{TENS_IN_ENGLISH[tens * 10]}-{NUMBERS_IN_ENGLISH[units]}"
