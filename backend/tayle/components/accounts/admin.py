from django.contrib import admin

from .models import AccountList

class AccountListAdmin(admin.ModelAdmin):
    list_display = ('_id', 'status', 'currency', 'user', 'balance')

admin.site.register(AccountList, AccountListAdmin)