from django.shortcuts import render
from rest_framework import viewsets
from metro.serializers import MetroSerializer, CountrySerializer, TownSerializer
from metro.models import Metro, Country, Town


class MetroViewSet(viewsets.ModelViewSet):
  queryset = Metro.objects.all()
  serializer_class = MetroSerializer


class CountryViewSet(viewsets.ModelViewSet):
  queryset = Country.objects.all()
  serializer_class = CountrySerializer


class TownViewSet(viewsets.ModelViewSet):
  queryset = Town.objects.all()
  serializer_class = TownSerializer

# Create your views here.
