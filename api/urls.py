from django.urls import path

from .views import get_condominium_expenses, make_expenses_prediction

urlpatterns = [
    path('api/v1/', get_condominium_expenses),
    path('api/v1/predict/', make_expenses_prediction),
]
