from django.shortcuts import render
from .serializers import PetoSerilizer
from rest_framework import generics
from .models import PetoCreate


class PetoGetCreate(generics.ListCreateAPIView):
    queryset=PetoCreate.objects.all()
    serializer_class=PetoSerilizer


class PetoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=PetoCreate.objects.all()
    serializer_class=PetoSerilizer
        
