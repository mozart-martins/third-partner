import uuid
from datetime import date
from core.models.Service import Service
from django.db import models
from users.models.coworkermodel import CoworkerModel


def user_directory_path(instance, filename):
    path = f'pdf/{date.today().year}/'
    print(path)
    return f'{path}{uuid.uuid4()}.pdf'


class ReceiptsModel(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    coworker = models.OneToOneField(CoworkerModel, on_delete=models.DO_NOTHING)
    hours_taken = models.TimeField()
    receipt = models.FileField(
        upload_to=user_directory_path)

    class Meta:
        verbose_name = "Recibo"
        verbose_name_plural = "Recibos"

    def __str__(self) -> str:
        return f"{self.service}, {self.coworker}"
