from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WorkedHours(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    worked_hours = models.TimeField()
    description = models.CharField(max_length=200)

    class Meta():
        verbose_name = "Hora"
        verbose_name_plural = "Horas"

    def __str__(self) -> str:
        return f"{self.worker}, {self.worked_hours}"

class WisdomQuotation(models.Model):
    quote = models.CharField(max_length=300)
    author = models.CharField(max_length=80)

    class Meta():
        verbose_name = "Citação"
        verbose_name_plural = "Citações"

    def __str__(self) -> str:
        return f"{self.quote}, {self.author}"