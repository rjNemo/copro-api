from rest_framework.decorators import api_view
from rest_framework.response import Response

from .data.prediction import LinearRegressor
from .data.statistics import get_condo_expenses_by


@api_view(['GET', 'POST'])
def get_condominium_expenses(request):
    """TODO: refactor using APIView class"""

    data = {}
    if request.method == "POST":
        query_type = request.data["query_type"]
        query_val = request.data['query_val']

        data = get_condo_expenses_by(query_type, query_val)

    return Response(data)


@api_view(['POST'])
def make_expenses_prediction(request):
    """Return condominium expenses prediction."""

    algo = LinearRegressor
    prediction = algo.predict_expenses(request.data)

    return Response(prediction)
