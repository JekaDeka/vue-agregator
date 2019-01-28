from rest_framework import serializers
from device.models import Brand, Mark, SparePart, DeviceModel, DeviceType, DeviceAffiliation


class DeviceAffiliationSerializer(serializers.ModelSerializer):
  class Meta:
    model = DeviceType
    fields = '__all__'


class DeviceTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = DeviceType
    fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
  class Meta:
    model = Brand
    fields = '__all__'


class DeviceModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = DeviceModel
    fields = '__all__'


class SparePartSerialzer(serializers.ModelSerializer):
  class Meta:
    model = SparePart
    fields = '__all__'


class MarkSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mark
    fields = '__all__'
