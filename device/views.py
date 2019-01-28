from django.shortcuts import render
from rest_framework import viewsets
from device.models import Brand, DeviceModel, SparePart, Mark, DeviceType, DeviceAffiliation
from device.serializers import MarkSerializer, BrandSerializer, DeviceModelSerializer, SparePartSerialzer, DeviceTypeSerializer, DeviceAffiliationSerializer
from rest_framework import status


class DeviceAffiliationViewSet(viewsets.ModelViewSet):
  """
  API для всех брендов
  """
  queryset = DeviceAffiliation.objects.all()
  serializer_class = DeviceAffiliationSerializer


class DeviceTypeViewSet(viewsets.ModelViewSet):
  """
  API для всех брендов
  """
  queryset = DeviceType.objects.all()
  serializer_class = DeviceTypeSerializer


class BrandViewSet(viewsets.ModelViewSet):
  """
  API для всех брендов
  """
  queryset = Brand.objects.all()
  serializer_class = BrandSerializer


class DeviceModelViewSet(viewsets.ModelViewSet):
  """
  API для все моделей устройств
  """
  queryset = DeviceModel.objects.all()
  serializer_class = DeviceModelSerializer


class SparePartViewSet(viewsets.ModelViewSet):
  """
  API для все поломанных частей
  """
  queryset = SparePart.objects.all()
  serializer_class = SparePartSerialzer


class MarkViewSet(viewsets.ModelViewSet):
  """
  API для все поломанных частей
  """
  queryset = Mark.objects.all()
  serializer_class = MarkSerializer
