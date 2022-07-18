from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HoraTrabalhada(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    worked_hours = models.CharField(max_length=5)
    description = models.CharField(max_length=200)

    class Meta():
        verbose_name = "Hora"
        verbose_name_plural = "Horas"

    def __str__(self) -> str:
        return f"{self.worker}, {self.worked_hours}"
