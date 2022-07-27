from django.contrib import admin

from core.models import ReceiptsModel, WisdomQuotation, WorkedHours

admin.site.register(WorkedHours)
admin.site.register(WisdomQuotation)
admin.site.register(ReceiptsModel)
