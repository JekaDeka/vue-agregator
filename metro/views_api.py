from rest_framework import generics
from .serializers import CountrySerializer, TownSerializer, MetroSerializer
from .models import Country, Town, Metro


class TownByCountru(generics.ListAPIView):
  serializer_class = TownSerializer

  def get_queryset(self):
    id = self.kwargs['id']

    return Town.objects.filter(country_id=id)


class MetroByTown(generics.ListAPIView):
  serializer_class = MetroSerializer

  def get_queryset(self):
    id = self.kwargs['id']

    return Metro.objects.filter(town_id=id)


class MetroByTownName(generics.ListAPIView):
  serializer_class = MetroSerializer

  def get_queryset(self):
    name = self.kwargs['town']
    town = Town.objects.get(name=name)
    return Metro.objects.filter(town_id=town.id)


class MetroFilter(generics.ListAPIView):
  serializer_class = MetroSerializer

  def get_queryset(self):
    metro = self.kwargs['name']

    return Metro.objects.filter(name=metro)


class TownByCountryName(generics.ListAPIView):
  serializer_class = TownSerializer

  def get_queryset(self):
    name = self.kwargs['name']
    country = Country.objects.get(name=name)
    return Town.objects.filter(country_id=country.id)
