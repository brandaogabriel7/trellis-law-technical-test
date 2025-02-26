from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..domain.english_numbers.english_numbers import get_english_number
from django.conf import settings
from .validators import validate_integer

import time


@api_view(["GET", "POST"])
def num_in_english(request):
    if request.method == "GET":
        return __get_num_in_english(request)

    if request.method == "POST":
        return __post_num_in_english(request)

    return Response({"status": "error", "error": "Method not allowed"}, status=405)


def __get_num_in_english(request):
    number_param = request.query_params.get("number")
    if not number_param:
        return Response({"status": "error", "error": "Missing number"}, status=400)

    try:
        validate_integer(number_param)
        number = int(number_param)
        num_in_english = get_english_number(number)

        return Response({"status": "ok", "num_in_english": num_in_english})
    except ValueError as ve:
        return Response({"status": "error", "error": ve.args[0]}, status=400)


def __post_num_in_english(request):
    number_param = request.data.get("number")
    if not number_param:
        return Response({"status": "error", "error": "Missing number"}, status=400)

    try:
        validate_integer(number_param)
        number = int(number_param)

        # this was required in the test instructions
        time.sleep(settings.DELAY_TIME)

        num_in_english = get_english_number(number)
        return Response({"status": "ok", "num_in_english": num_in_english})
    except ValueError as ve:
        return Response({"status": "error", "error": ve.args[0]}, status=400)
