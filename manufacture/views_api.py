from rest_framework import generics
from .models import Manufacture, Master, Number
from .serializers import ManufactureSerializer, MasterSerializer, NumberSerializer


class ManufactureFilterByLogin(generics.ListAPIView):
  serializer_class = ManufactureSerializer

  def get_queryset(self):
    log = self.kwargs['login']
    return Manufacture.objects.filter(login=log)


class MasterFilterByLogin(generics.ListAPIView):
  serializer_class = MasterSerializer

  def get_queryset(self):
    log = self.kwargs['login']
    return Master.objects.filter(login=log)


class NumbersByManufacture(generics.ListAPIView):
  serializer_class = NumberSerializer

  def get_queryset(self):
    id = self.kwargs['id']

    return Number.objects.filter(manufacture_id=id)


class NumbersByMaster(generics.ListAPIView):
  serializer_class = NumberSerializer

  def get_queryset(self):
    id = self.kwargs['id']

    return Number.objects.filter(master_id=id)


class ManufactureByLoginPassword(generics.ListAPIView):
  serializer_class = ManufactureSerializer

  def get_queryset(self):
    login = self.kwargs['login']
    password = self.kwargs['password']
    return Manufacture.objects.filter(login=login, password=password)


class MasterByLoginPassword(generics.ListAPIView):
  serializer_class = MasterSerializer

  def get_queryset(self):
    login = self.kwargs['login']
    password = self.kwargs['password']
    return Master.objects.filter(login=login, password=password)
