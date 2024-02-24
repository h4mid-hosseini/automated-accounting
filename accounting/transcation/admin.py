from django.contrib import admin
from . import models

class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('title','price','is_cost','created_at')
    search_fields = ('title',)
    



admin.site.register(models.Transactions, TransactionsAdmin)
admin.site.register(models.Types)