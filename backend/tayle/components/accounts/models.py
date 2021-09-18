from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

STATUS = (
    ('active', "Активный"),
    ('blocked', "Заблокированный"),
    ('closed', "Закрытый"),
)
CURRENCY = (
    ('rub', "Рубли"),
)

class AccountList(models.Model):
    _id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=7, choices=STATUS, null=False, blank=False, default="active")
    currency = models.CharField(max_length=3, choices=CURRENCY, null=False, blank=False, default="rub")
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    sum = models.FloatField(null=False, blank=False)

    def __str__(self):
        return "{}".format(self._id)

    class Meta:
        db_table = 'account_list'
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'


class AccountMovements(models.Model):
    _id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(AccountList, related_name='sender', on_delete=models.PROTECT, null=False, blank=False)
    recipient = models.ForeignKey(AccountList, related_name='recipient', on_delete=models.PROTECT, null=False, blank=False)
    sum = models.FloatField(null=False, blank=False)
    time_created = models.TimeField(auto_now_add=True)

    class Meta:
        db_table = 'account_movements'
        verbose_name = 'Движение по счету'
        verbose_name_plural = 'Движение по счетам'
