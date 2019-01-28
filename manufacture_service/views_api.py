from rest_framework import generics
from device.models import DeviceAffiliation, DeviceType, DeviceModel, SparePart
from .serializers import FaultSerializer, ManufactureServiceSerializer, BreakageAtionSerializer
from .models import Fault, ManufactureService, BreakageAtion


class FaultByDeviceModel(generics.ListAPIView):
  serializer_class = FaultSerializer

  def get_queryset(self):
    device_model = DeviceModel.objects.get(id=self.kwargs['id'])
    mark_id = device_model.mark
    return Fault.objects.filter(mark_id=mark_id)


class ManufactureServiceByDeviceModel(generics.ListAPIView):
  serializer_class = ManufactureServiceSerializer

  def get_queryset(self):
    device_model = DeviceModel.objects.get(id=self.kwargs['id'])
    mark_id = device_model.mark
    return ManufactureService.objects.filter(mark_id=mark_id)


class BreakageAtionByDeviceModel(generics.ListAPIView):
  serializer_class = BreakageAtionSerializer

  def get_queryset(self):
    device_model = DeviceModel.objects.get(id=self.kwargs['id'])
    mark_id = device_model.mark
    return BreakageAtion.objects.filter(mark_id=mark_id)


class BreakageActionByFault(generics.ListAPIView):

  serializer_class = BreakageAtionSerializer

  def get_queryset(self):
    id = self.kwargs['id']
    return BreakageAtion.objects.filter(fault_id=id)


class FaultsBySparePart(generics.ListAPIView):
  serializer_class = FaultSerializer

  def get_queryset(self):
    id = self.kwargs['id']
    return Fault.objects.filter(spare_part_id=id)


class FaultFilter(generics.ListAPIView):
  serializer_class = FaultSerializer

  def get_queryset(self):
    fault = self.kwargs['name']

    return Fault.objects.filter(name=fault)


class BreakageAtionByMark(generics.ListAPIView):
  serializer_class = BreakageAtionSerializer

  def get_queryset(self):
    id = self.kwargs['id']

    return BreakageAtion.objects.filter(mark_id=id)


class ManufactureServiceByManufacture(generics.ListAPIView):
  serializer_class = ManufactureServiceSerializer

  def get_queryset(self):
    id = self.kwargs['id']
    return ManufactureService.objects.filter(manufacture_id=id)
