from rest_framework import generics
from device.serializers import DeviceTypeSerializer, BrandSerializer, DeviceModelSerializer, SparePartSerialzer, MarkSerializer
from device.models import DeviceAffiliation, DeviceType, DeviceModel, Brand, SparePart, Mark


class DeviceTypesByAffilication(generics.ListAPIView):
  serializer_class = DeviceTypeSerializer

  def get_queryset(self):
    id = self.kwargs['id']
    return DeviceType.objects.filter(device_affilication_id=id)


class BrandsByDeviceType(generics.ListAPIView):
  serializer_class = BrandSerializer

  def get_queryset(self):
    id = self.kwargs['id']
    return Brand.objects.filter(device_type_id=id)


class DeviceModelByBrandDeviceType(generics.ListAPIView):
  serializer_class = DeviceModelSerializer

  def get_queryset(self):
    device_type_id = self.kwargs['id_device_type']
    brand_id = self.kwargs['id_brand']
    return DeviceModel.objects.filter(brand_id=brand_id, device_type_id=device_type_id)


class SparePartByDeviceModel(generics.ListAPIView):
  serializer_class = SparePartSerialzer

  def get_queryset(self):
    id = self.kwargs['id']
    device_model = DeviceModel.objects.get(id=id)
    mark_id = device_model.mark
    return SparePart.objects.filter(mark_id=mark_id)


class DeviceTypeFilter(generics.ListAPIView):
  serializer_class = DeviceTypeSerializer

  def get_queryset(self):
    aff = self.kwargs['name']

    return DeviceType.objects.filter(name=aff)


class BrandFilter(generics.ListAPIView):
  serializer_class = BrandSerializer

  def get_queryset(self):
    brand = self.kwargs['name']

    return Brand.objects.filter(name=brand)


class DeviceModelFilter(generics.ListAPIView):
  serializer_class = DeviceModelSerializer

  def get_queryset(self):
    device = self.kwargs['name']

    return DeviceModel.objects.filter(name=device)


class MarkByBrand(generics.ListAPIView):
  serializer_class = MarkSerializer

  def get_queryset(self):
    id = self.kwargs['id']
    return Mark.objects.filter(brand_id=id)
