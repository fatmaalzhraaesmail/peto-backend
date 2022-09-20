from dataclasses import fields
from . models import AccountCreate
from rest_framework import serializers
class AccountSerilizer(serializers.ModelSerializer):
    class Meta:
        model=AccountCreate
        fields='__all__'