from django.shortcuts import render
from rest_framework import viewsets
from manufacture.serializers import ManufactureSerializer, MasterSerializer, NumberSerializer
from manufacture.models import Manufacture, Master, Number
from rest_framework.permissions import AllowAny


class ManufactureViewSet(viewsets.ModelViewSet):
  """
  API для сервисов
  """
  permission_classes = (AllowAny,)
  queryset = Manufacture.objects.all()
  serializer_class = ManufactureSerializer


class MasterViewSet(viewsets.ModelViewSet):
  """
  API для мастеров
  """
  permission_classes = (AllowAny,)
  queryset = Master.objects.all()
  serializer_class = MasterSerializer


class NumberViewSet(viewsets.ModelViewSet):
  permission_classes = (AllowAny,)
  queryset = Number.objects.all()
  serializer_class = NumberSerializer
# Create your views here.
