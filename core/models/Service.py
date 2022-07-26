from django.db import models
from users.models.coworkermodel import CoworkerModel


class Service(models.Model):
    coworker = models.ForeignKey(CoworkerModel, on_delete=models.CASCADE)
    service = models.CharField(max_length=80, required=True)
    description = models.CharField(max_length=500)
    price = models.FloatField()

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self) -> str:
        return f"{self.service}, {self.coworker}"
