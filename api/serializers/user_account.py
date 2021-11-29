from rest_framework import serializers
from account.models import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = (
            'first_name',
            'last_name',
            'email',
            'password'
        )


class PasswordResetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ("email", 'password')