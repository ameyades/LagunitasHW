from django.db import models


class Rating(models.Model):
    beer_name = models.CharField(max_length=30)
    score = models.DecimalField(max_digits=2, decimal_places=1)
    brewer_name = models.CharField(max_length=30)
    notes = models.CharField(max_length=50)


