from django.urls import path
from django.views.generic import TemplateView

app_name = 'core'

urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html'), name='index_view'),
    path('footer/', TemplateView.as_view(template_name='core/footer.html'), name='footer'),
]
