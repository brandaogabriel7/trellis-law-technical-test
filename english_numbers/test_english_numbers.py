import pytest

from english_numbers.english_numbers import english_number


def test_error_when_number_is_negative():
    with pytest.raises(ValueError):
        english_number(-1)


@pytest.mark.parametrize("number,number_in_english", [(0, "zero"), (1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five"), (6, "six"), (7, "seven"), (8, "eight"), (9, "nine")])
def test_numbers_from_0_to_9(number, number_in_english):
    assert english_number(number) == number_in_english


@pytest.mark.parametrize("number,number_in_english", [
    (10, "ten"),
    (11, "eleven"),
    (12, "twelve"),
    (13, "thirteen"),
    (14, "fourteen"),
    (15, "fifteen"),
    (16, "sixteen"),
    (17, "seventeen"),
    (18, "eighteen"),
    (19, "nineteen")])
def test_numbers_from_10_to_19(number, number_in_english):
    assert english_number(
        number) == number_in_english, f"Expected '{number_in_english}' but got '{english_number(number)}'"


@pytest.mark.parametrize("number,number_in_english", [
    (20, "twenty"),
    (21, "twenty-one"),
    (22, "twenty-two"),
    (23, "twenty-three"),
    (24, "twenty-four"),
    (25, "twenty-five"),
    (26, "twenty-six"),
    (27, "twenty-seven"),
    (28, "twenty-eight"),
    (29, "twenty-nine"),
    (30, "thirty"),
    (31, "thirty-one"),
    (40, "forty"),
    (42, "forty-two"),
    (50, "fifty"),
    (53, "fifty-three"),
    (60, "sixty"),
    (70, "seventy"),
    (80, "eighty"),
    (90, "ninety"),
    (99, "ninety-nine")
])
def test_numbers_from_20_to_99(number, number_in_english):
    assert english_number(
        number) == number_in_english, f"Expected '{number_in_english}' but got '{english_number(number)}'"


@pytest.mark.parametrize("number,number_in_english", [
    (100, "one hundred"),
    (101, "one hundred and one"),
    (110, "one hundred and ten"),
    (111, "one hundred and eleven"),
    (120, "one hundred and twenty"),
    (121, "one hundred and twenty-one"),
    (200, "two hundred"),
    (300, "three hundred"),
    (400, "four hundred"),
    (500, "five hundred"),
    (505, "five hundred and five"),
    (600, "six hundred"),
    (700, "seven hundred"),
    (724, "seven hundred and twenty-four"),
    (800, "eight hundred"),
    (900, "nine hundred"),
    (999, "nine hundred and ninety-nine")
])
def test_numbers_from_100_to_999(number, number_in_english):
    assert english_number(
        number) == number_in_english, f"Expected '{number_in_english}' but got '{english_number(number)}'"


@pytest.mark.parametrize("number,number_in_english", [
    (1000, "one thousand"),
    (1001, "one thousand one"),
    (1010, "one thousand ten"),
    (1100, "one thousand one hundred"),
    (1111, "one thousand one hundred and eleven"),
    (1200, "one thousand two hundred"),
    (1210, "one thousand two hundred and ten"),
    (2000, "two thousand"),
    (3000, "three thousand"),
    (4000, "four thousand"),
    (5000, "five thousand"),
    (6000, "six thousand"),
    (7000, "seven thousand"),
    (8000, "eight thousand"),
    (9000, "nine thousand"),
    (9999, "nine thousand nine hundred and ninety-nine"),
    (10000, "ten thousand"),
    (10001, "ten thousand one"),
    (10100, "ten thousand one hundred"),
    (11000, "eleven thousand"),
    (11100, "eleven thousand one hundred"),
    (11110, "eleven thousand one hundred and ten"),
    (11111, "eleven thousand one hundred and eleven"),
    (12000, "twelve thousand"),
    (12100, "twelve thousand one hundred"),
    (12110, "twelve thousand one hundred and ten"),
    (12111, "twelve thousand one hundred and eleven"),
    (20000, "twenty thousand"),
    (30000, "thirty thousand"),
    (40000, "forty thousand"),
    (50000, "fifty thousand"),
    (60000, "sixty thousand"),
    (70000, "seventy thousand"),
    (79233, "seventy-nine thousand two hundred and thirty-three"),
    (80000, "eighty thousand"),
    (90000, "ninety thousand"),
    (99999, "ninety-nine thousand nine hundred and ninety-nine"),
    (123456, "one hundred and twenty-three thousand four hundred and fifty-six"),
    (999999, "nine hundred and ninety-nine thousand nine hundred and ninety-nine"),
    (999999999, "nine hundred and ninety-nine million nine hundred and ninety-nine thousand nine hundred and ninety-nine"),
    (999999999999, "nine hundred and ninety-nine billion nine hundred and ninety-nine million nine hundred and ninety-nine thousand nine hundred and ninety-nine"),
    (999999999999999, "nine hundred and ninety-nine trillion nine hundred and ninety-nine billion nine hundred and ninety-nine million nine hundred and ninety-nine thousand nine hundred and ninety-nine"),
    (999999999999999999, "nine hundred and ninety-nine quadrillion nine hundred and ninety-nine trillion nine hundred and ninety-nine billion nine hundred and ninety-nine million nine hundred and ninety-nine thousand nine hundred and ninety-nine")
])
def test_numbers_from_1000_to_999999(number, number_in_english):
    assert english_number(
        number) == number_in_english, f"Expected '{number_in_english}' but got '{english_number(number)}'"
