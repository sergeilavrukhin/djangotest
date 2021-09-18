from django.contrib import admin

from .models import AccountList

class AccountListAdmin(admin.ModelAdmin):
    list_display = ('_id', 'status', 'currency', 'user', 'sum')

admin.site.register(AccountList, AccountListAdmin)