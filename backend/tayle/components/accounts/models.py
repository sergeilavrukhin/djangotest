from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

User = get_user_model()

STATUS = (
    ('active', "Активный"),
    ('blocked', "Заблокированный"),
    ('closed', "Закрытый"),
)

CURRENCY = (
    ('rub', "Рубли"),
)

TYPE_MOVEMENT = (
    ('debited', "Списаны"),
    ('credited', "Зачислены"),
)

class AccountList(models.Model):
    _id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=7, choices=STATUS, null=False, blank=False, default="active")
    currency = models.CharField(max_length=3, choices=CURRENCY, null=False, blank=False, default="rub")
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    balance = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return "{} {}".format(self._id, self.user)

    def get_id(self):
        return self._id

    class Meta:
        db_table = 'account_list'
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'


class AccountMovements(models.Model):
    _id = models.AutoField(primary_key=True)
    account = models.ForeignKey(AccountList, related_name='account', on_delete=models.PROTECT, null=True, blank=False)
    related_account = models.ForeignKey(AccountList, related_name='related_account', on_delete=models.PROTECT, null=True, blank=False)
    sum = models.FloatField(null=False, blank=False)
    type = models.CharField(max_length=8, choices=TYPE_MOVEMENT, null=False, blank=False, default="credited")
    date_created = models.DateField(auto_now_add=True)
    time_created = models.TimeField(auto_now_add=True)

    class Meta:
        db_table = 'account_movements'
        verbose_name = 'Движение по счету'
        verbose_name_plural = 'Движение по счетам'
