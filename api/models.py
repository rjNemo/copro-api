from django.db import models


class CondominiumExpense(models.Model):
    mean = models.FloatField()
    first_quantile = models.FloatField()
    ninth_quantile = models.FloatField()


class CondominiumExpenseQuery(models.Model):
    QUERY_TYPES = [
        ('DEPT_CODE', 'Department'),
        ('ZIP_CODE', 'Postal Code'),
        ('CITY', 'City'),
    ]
    query_type = models.CharField(
        max_length=20, choices=QUERY_TYPES, default='DEPT_CODE')
    value = models.CharField(max_length=40, blank=True, default="")
