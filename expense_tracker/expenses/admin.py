from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'amount', 'type', 'payment_method', 'is_deleted')
    list_filter = ('type', 'category', 'payment_method')
    search_fields = ('description',)
