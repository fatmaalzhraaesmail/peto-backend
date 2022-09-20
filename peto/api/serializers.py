# from dataclasses import fields
from . models import PetoCreate
from rest_framework import serializers
class PetoSerilizer(serializers.ModelSerializer):
    class Meta:
        model=PetoCreate
        fields='__all__'