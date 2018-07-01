from django.contrib import admin

from .models import Account, Withdrawal, Category, Transaction

admin.site.site_header = 'Expenser Dashboard'


admin.site.register(Account)
admin.site.register(Withdrawal)
admin.site.register(Category)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'category')
    list_filter = ('date', 'category',)
    # search_fields = ('date', 'amount', 'category')


admin.site.register(Transaction, TransactionAdmin)
