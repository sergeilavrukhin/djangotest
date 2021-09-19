from .models import AccountList
from rest_framework import serializers


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountList
        fields = ('_id', 'balance', 'currency', 'user')
