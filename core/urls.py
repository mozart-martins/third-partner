from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (AddHoursView, HomeView, ReceiptView, SheetView,
                    VacanciesView)

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="index_view"),
    path("planilha/", SheetView.as_view(), name="sheet_view"),
    path("notas/", ReceiptView.as_view(), name="receipt_view"),
    path("vagas/", VacanciesView.as_view(), name="vacancies_view"),
    path(
        "planilha/adicionarhoras",
        login_required(AddHoursView.as_view()),
        name="add_hours_view",
    ),
]
