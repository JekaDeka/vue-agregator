from rest_framework import serializers
from metro.models import Metro, Country, Town


class MetroSerializer(serializers.ModelSerializer):
  class Meta:
    model = Metro
    fields = '__all__'


class TownSerializer(serializers.ModelSerializer):
  class Meta:
    model = Town
    fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
  class Meta:
    model = Country
    fields = '__all__'
