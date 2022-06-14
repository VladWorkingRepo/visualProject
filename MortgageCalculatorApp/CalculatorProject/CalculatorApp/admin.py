from django.contrib import admin

from .models import *
# Register your models here.


@admin.register(Banks)
class BanksAdmin(admin.ModelAdmin):
    list_display = ('id', 'bank_name', 'interest_rate')
    list_filter = ('bank_name', 'interest_rate')
