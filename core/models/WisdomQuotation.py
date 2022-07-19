from django.db import models


class WisdomQuotation(models.Model):
    quote = models.CharField(max_length=300)
    author = models.CharField(max_length=80)

    class Meta():
        verbose_name = "Citação"
        verbose_name_plural = "Citações"

    def __str__(self) -> str:
        return f"{self.quote}, {self.author}"
