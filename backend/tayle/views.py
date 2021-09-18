from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .components.accounts.models import AccountList

def index(request):
    return render(request, 'index.html')


@login_required
def profile(request):
    balans = AccountList.objects.filter(user=request.user).aggregate(Sum('sum'))
    return render(request, 'registration/profile.html', {'balans': balans["sum__sum"]})
