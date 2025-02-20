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
    9: "nine"
}


def write_number_in_english(number: int) -> str:
    return numbers_in_english[number]
