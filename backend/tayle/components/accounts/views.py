from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from rest_framework import generics

from .models import AccountList, AccountMovements
from .filters import AccountListFilter, AccountMovementsFilter
from .forms import AccountSearchForm
from .serializers import AccountListSerializer


@login_required
def accounts_list(request):
    accounts_list = AccountListFilter(request.GET, queryset=AccountList.objects.filter(user=request.user).all())
    return render(request, 'accounts/list.html', {'accounts_list': accounts_list})


@login_required
def account_movements(request):
    filter = AccountMovementsFilter(request.GET, queryset=AccountMovements.objects.filter(
        account__in=set(AccountList.objects.filter(user=request.user).all())).order_by("time_created").all())

    paginator = Paginator(filter.qs, 5)
    page = request.GET.get('page', 1)
    account_movements = paginator.get_page(page)

    params = "type={}&sum={}&date_created_day={}&date_created_month={}&date_created_year={}" \
        .format(request.GET.get("type", ""), request.GET.get("sum", ""), request.GET.get("date_created_day", ""),
                request.GET.get("date_created_month", ""), request.GET.get("date_created_year", ""))

    return render(request, 'accounts/movements.html',
                  {'form': filter.form, 'account_movements': account_movements, 'params': params})


@login_required
def account_detail(request, id):
    try:
        account = AccountList.objects.get(_id=id, user=request.user)
    except ValueError:
        account = None
    return render(request, 'accounts/detail.html', {'account': account})


@login_required
def account_send(request):
    error = ""
    sum_account = 0
    sender_ids_list = None
    if request.method == 'POST':
        if ('account_recipient' in request.POST) is False:
            error += 'Выберите счет получателя<br />'

        if ('account_sender' in request.POST) is False:
            error += 'Выберите хотя бы один счет отправителя<br />'

        try:
            sum = float(request.POST['sum'])
        except ValueError:
            sum = 0

        if sum <= 0:
            error += 'Введите сумму, которую необходимо перевести<br />'

        sender_ids_list = request.POST.getlist('account_sender')
        if len(sender_ids_list) > 0:
            if sum % len(sender_ids_list) != 0:
                error += 'Сумма не делится в равных долях между счетами<br />'

            # Сумма, которая будет списана со счета
            sum_account = sum / len(sender_ids_list)

            # Проверка наличия необходимой суммы на балансе счета
            for sender_id in sender_ids_list:
                sender = AccountList.objects.get(_id=sender_id)
                if sender.balance < sum_account:
                    error += "На счете {} недостаточно средств для перевода<br />".format(sender_id)

        if error == "":
            # Пополнение баланса получателя
            account_recipient = AccountList.objects.get(_id=request.POST['account_recipient'])
            account_recipient.balance = account_recipient.balance + sum
            account_recipient.save()
            for sender_id in sender_ids_list:

                # Снятие со счета необходимой суммы
                account_sender = AccountList.objects.get(_id=sender_id)
                account_sender.balance = account_sender.balance - sum_account
                account_sender.save()

                # Движение-списание со счета отправителя на счет получателя
                account_movements_debited = AccountMovements(account=account_sender, related_account=account_recipient,
                                                             sum=sum_account, type='debited')
                account_movements_debited.save()

                # Движение-зачисление на счет получателя со счета отправителя
                account_movements_credited = AccountMovements(account=account_recipient, related_account=account_sender,
                                                              sum=sum_account, type='credited')
                account_movements_credited.save()

            return render(request, 'accounts/transaction_success.html')

    form = AccountSearchForm()
    if 'query' in request.GET:
        form = AccountSearchForm(request.GET)
        try:
            accounts_recipient_list = AccountList.objects.filter(
                ~Q(user=request.user),
                Q(_id=int(request.GET["query"]))).all()
        except ValueError:
            accounts_recipient_list = None
    else:
        accounts_recipient_list = AccountList.objects.filter(~Q(user=request.user)).all()

    accounts_sender_list = AccountList.objects.filter(user=request.user).all()

    return render(request, 'accounts/send.html', {'error': error, 'form': form, 'sender_ids_list': sender_ids_list,
                                                  'accounts_sender_list': accounts_sender_list,
                                                  'accounts_recipient_list': accounts_recipient_list})


class AccountListDRF(generics.ListCreateAPIView):
    queryset = AccountList.objects.all()
    serializer_class = AccountListSerializer
