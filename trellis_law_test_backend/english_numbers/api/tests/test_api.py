from django.urls import reverse
import pytest
from django.test import override_settings

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

def num_in_english_success_data():
    return [
        (0, "zero"),
        (1, "one"),
        (999, "nine hundred and ninety-nine"),
        (42349, "forty-two thousand three hundred and forty-nine"),
        (10000000, "ten million"),
        (123456789, "one hundred and twenty-three million four hundred and fifty-six thousand seven hundred and eighty-nine"),
    ]

@pytest.mark.parametrize("number,expected", num_in_english_success_data())
def test_get_numInEnglish_success(api_client, number, expected):
    url = reverse("num-in-english")
    response = api_client.get(f'{url}?number={number}')

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "num_in_english": expected}

def test_get_numInEnglish_missingNumber(api_client):
    url = reverse("num-in-english")
    response = api_client.get(url)

    assert response.status_code == 400
    assert response.json() == {"status": "error", "message": "Missing number"}

def test_get_numInEnglish_invalidNumber(api_client):
    url = reverse("num-in-english")
    response = api_client.get(f'{url}?number=invalid')

    assert response.status_code == 400
    assert response.json() == {"status": "error", "message": "Invalid number"}

@pytest.mark.parametrize("number,expected", num_in_english_success_data())
@override_settings(DELAY_TIME=.001) # override the delay time to speed up the test
def test_post_numInEnglish_success(api_client, number, expected):
    url = reverse("num-in-english")
    response = api_client.post(url, {"number": number})

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "num_in_english": expected}