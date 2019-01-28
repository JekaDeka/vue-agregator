from rest_framework import serializers
from manufacture_service.models import Fault, ManufactureService, BreakageAtion


class FaultSerializer(serializers.ModelSerializer):
  class Meta:
    model = Fault
    fields = ('id', 'name',)


class ManufactureServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = ManufactureService
    fields = '__all__'


class BreakageAtionSerializer(serializers.ModelSerializer):
  class Meta:
    model = BreakageAtion
    fields = '__all__'
