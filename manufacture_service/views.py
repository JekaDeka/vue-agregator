from django.shortcuts import render
from rest_framework import viewsets
from manufacture_service.serializers import FaultSerializer, ManufactureServiceSerializer, BreakageAtionSerializer
from manufacture_service.models import Fault, ManufactureService, BreakageAtion
from rest_framework.permissions import AllowAny


class FaultViewSet(viewsets.ModelViewSet):
  """
  API для поломки
  """
  queryset = Fault.objects.all()
  serializer_class = FaultSerializer


class ManufactureServiceViewSet(viewsets.ModelViewSet):
  """
  API для услуги сервисов
  """
  permission_classes = (AllowAny,)
  queryset = ManufactureService.objects.all()
  serializer_class = ManufactureServiceSerializer


class BreakageAtionViewSet(viewsets.ModelViewSet):
  """
  API для действий по решению проблемы
  """
  queryset = BreakageAtion.objects.all()
  serializer_class = BreakageAtionSerializer
# Create your views here.
