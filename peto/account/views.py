from django.shortcuts import render
from .serializers import AccountSerilizer
from rest_framework import generics
from .models import AccountCreate


class AccountGetCreate(generics.ListCreateAPIView):
    queryset=AccountCreate.objects.all()
    serializer_class=AccountSerilizer


class AccountUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=AccountCreate.objects.all()
    serializer_class=AccountSerilizer
