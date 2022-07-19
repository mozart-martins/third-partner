from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class WorkedHours(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    worked_hours = models.TimeField()
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Hora"
        verbose_name_plural = "Horas"

    def __str__(self) -> str:
        return f"{self.worker}, {self.worked_hours}"
