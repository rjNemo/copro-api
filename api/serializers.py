from rest_framework import serializers

from .models import CondominiumExpense, CondominiumExpenseQuery


class CondominiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = CondominiumExpense
        fields = '__all__'


class CondominiumQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = CondominiumExpenseQuery
        fields = '__all__'
