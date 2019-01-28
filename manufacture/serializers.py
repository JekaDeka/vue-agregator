from rest_framework import serializers
from manufacture.models import Manufacture, Master, Number


class ManufactureSerializer(serializers.ModelSerializer):
  class Meta:
    model = Manufacture
    fields = '__all__'


class MasterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Master
    fields = '__all__'


class NumberSerializer (serializers.ModelSerializer):
  class Meta:
    model = Number
    fields = '__all__'
