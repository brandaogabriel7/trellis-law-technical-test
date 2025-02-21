import pytest

from english_numbers.english_numbers import english_number


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
        number) == number_in_english, f"Expected {number_in_english} but got {english_number(number)}"


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
        number) == number_in_english, f"Expected {number_in_english} but got {english_number(number)}"


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
        number) == number_in_english, f"Expected {number_in_english} but got {english_number(number)}"
