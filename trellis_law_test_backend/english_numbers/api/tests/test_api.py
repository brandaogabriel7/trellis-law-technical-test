from django.urls import reverse
import pytest

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

def test_getData(api_client):
    url = reverse("getData")
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json() == {"data": "Hello, world!"}

@pytest.mark.parametrize("number,expected", [
    (0, "zero"),
    # (1, "one"),
    # (10000000, "ten million"),
    # (123456789, "one hundred twenty-three million four hundred fifty-six thousand seven hundred eighty-nine"),
])
def test_getEnglishNumber(api_client, number, expected):
    url = reverse("getEnglishNumber")
    response = api_client.get(f'{url}?number={number}')

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "num_in_english": expected}