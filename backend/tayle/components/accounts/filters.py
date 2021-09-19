import django_filters
from django import forms

from .models import AccountList, AccountMovements, STATUS, TYPE_MOVEMENT


class AccountListFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(label='Статус', choices=STATUS,
                                         widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = AccountList
        fields = ['status']


class AccountMovementsFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(label='Тип движения', choices=TYPE_MOVEMENT,
                                       widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    sum = django_filters.NumberFilter(label='Сумма')
    date_created = django_filters.DateFilter(label='Дата и время создания', widget=forms.SelectDateWidget)

    class Meta:
        model = AccountMovements
        fields = ['type', 'sum', 'date_created']
