import django_filters
from django import forms

from .models import AccountList, STATUS

class AccountListFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(label='Статус', choices=STATUS, widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    class Meta:
        model = AccountList
        fields = ['status']