from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import AccountList
from .filters import AccountListFilter

@login_required
def accounts_list(request):
    accounts_list = AccountListFilter(request.GET, queryset=AccountList.objects.filter(user=request.user).all())
    return render(request, 'accounts/list.html', {'accounts_list': accounts_list})

@login_required
def account_one(request, id):
    account = AccountList.objects.get(_id=id)
    return render(request, 'accounts/one.html', {'account': account})
