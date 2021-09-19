from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .components.accounts.models import AccountList, AccountMovements

def index(request):
    return render(request, 'index.html')


@login_required
def profile(request):
    balance = AccountList.objects.filter(user=request.user).aggregate(Sum('balance'))
    account_movements = AccountMovements.objects.filter(account__in=set(AccountList.objects.filter(user=request.user).all())).all().order_by("-time_created")[:5]

    return render(request, 'registration/profile.html', {'balance': balance["balance__sum"], 'account_movements': account_movements})
