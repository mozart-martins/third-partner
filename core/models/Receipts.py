from django.db import models

from .Service import Service


class Receipts(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    coworker = models.
    hours_taken = models.TimeField()

    class Meta:
        verbose_name = "Citação"
        verbose_name_plural = "Citações"

    def __str__(self) -> str:
        return f"{self.quote}, {self.author}"
