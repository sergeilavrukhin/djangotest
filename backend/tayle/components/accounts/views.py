from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import get_user_model

from .models import AccountList
from .filters import AccountListFilter
from .forms import AccountSearchForm, AccountListForm

User = get_user_model()

@login_required
def accounts_list(request):
    accounts_list = AccountListFilter(request.GET, queryset=AccountList.objects.filter(user=request.user).all())
    return render(request, 'accounts/list.html', {'accounts_list': accounts_list})

@login_required
def account_detail(request, id):
    try:
        account = AccountList.objects.get(_id=id, user=request.user)
    except:
        account = None
    return render(request, 'accounts/detail.html', {'account': account})

@login_required
def account_send(request):
    error = None
    sender_list = None
    if request.method == 'POST':
        recipient = None
        if 'account_recipient' in request.POST:
            if 'account_sender' in request.POST:
                sender_list = request.POST.getlist('account_sender')
                try:
                    sum = float(request.POST['sum'])
                except:
                    sum = 0
                if sum > 0:
                    recipient = AccountList.objects.get(_id=request.POST['account_recipient'])
                else:
                    error = 'Введите сумму, которую необходимо перевести'
            else:
                error = 'Выберите хотя бы один счет отправителя'
        else:
            error = 'Выберите счет получателя'

        if error is None:
            return render(request, 'accounts/transaction_success.html', {'account': recipient})

    form = AccountSearchForm()
    if 'query' in request.GET:
        form = AccountSearchForm(request.GET)
        try:
            accounts_recipient_list = AccountList.objects.filter(~Q(user=request.user), Q(_id=int(request.GET["query"]))).all()
        except:
            accounts_recipient_list = None
    else:
        accounts_recipient_list = AccountList.objects.filter(~Q(user=request.user)).all()

    accounts_sender_list = AccountList.objects.filter(user=request.user).all()

    return render(request, 'accounts/send.html', {'error': error, 'form': form, 'sender_list': sender_list, 'accounts_sender_list': accounts_sender_list, 'accounts_recipient_list': accounts_recipient_list})