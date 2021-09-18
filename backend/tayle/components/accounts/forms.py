from django import forms

from .models import AccountList, AccountMovements

class AccountListForm(forms.ModelForm):
    receive_newsletter = forms.BooleanField()
    class Meta:
        model = AccountList
        fields = ('_id', 'user', 'sum',)

class AccountMovementsForm(forms.ModelForm):
    class Meta:
        model = AccountMovements
        fields = ('_id', 'recipient', 'sum')

class AccountSearchForm(forms.Form):
    query = forms.CharField(label='Счет')