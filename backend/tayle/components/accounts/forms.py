from django import forms

class AccountSearchForm(forms.Form):
    query = forms.CharField(label='Счет')