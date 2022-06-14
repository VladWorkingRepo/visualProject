from django.db import models


class Banks(models.Model):
    """This is Banks model save next data: bank name and initial rate"""
    bank_name = models.CharField(max_length=60, blank=False)
    interest_rate = models.FloatField()

    class Meta:
        ordering = ['interest_rate']

    def __str__(self):
        return self.bank_name
