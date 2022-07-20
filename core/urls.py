from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from .views import AddHoursView, ReceiptView, SheetView, VacanciesView

app_name = "core"

urlpatterns = [
    path("", TemplateView.as_view(
        template_name="core/index.html"), name="index_view"),
    path("planilha/", SheetView.as_view(), name="sheet_view"),
    path("notas/", ReceiptView.as_view(), name="receipt_view"),
    path("vagas/", VacanciesView.as_view(), name="vacancies_view"),
    path("planilha/adicionarhoras", login_required(AddHoursView.as_view()),
         name="add_hours_view"),
]
