import pytest

from english_numbers.english_numbers import write_number_in_english


@pytest.mark.parametrize("number,number_in_english", [(0, "zero"), (1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five"), (6, "six"), (7, "seven"), (8, "eight"), (9, "nine")])
def test_numbers_from_0_to_9(number, number_in_english):
    assert write_number_in_english(number) == number_in_english
