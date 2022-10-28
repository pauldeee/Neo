from django.contrib import admin
from .models import Exchange


# Register your models here.
class ExchangeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Exchange, ExchangeAdmin)
