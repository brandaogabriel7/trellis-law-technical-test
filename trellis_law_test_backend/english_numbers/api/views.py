from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..domain.english_numbers.english_numbers import get_english_number

@api_view(['GET'])
def getData(request):
    return Response({"data": "Hello, world!"})

@api_view(['GET'])
def get_num_in_english(request):
    number_param = request.query_params.get('number')
    num_in_english = get_english_number(int(number_param))
    return Response({"status": "ok", "num_in_english": num_in_english})
