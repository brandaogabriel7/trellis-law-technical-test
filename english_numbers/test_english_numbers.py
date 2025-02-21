import pytest

from english_numbers.english_numbers import write_number_in_english


@pytest.mark.parametrize("number,number_in_english", [(0, "zero"), (1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five"), (6, "six"), (7, "seven"), (8, "eight"), (9, "nine")])
def test_numbers_from_0_to_9(number, number_in_english):
    assert write_number_in_english(number) == number_in_english


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
    assert write_number_in_english(number) == number_in_english


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
    assert write_number_in_english(number) == number_in_english
