from django.db import models
# from django.contrib.gis.geoip import GeoIP
from django.utils import timezone
from device.models import Brand, DeviceModel, Mark, DeviceType
from manufacture.models import Master, Manufacture
from manufacture_service.models import ManufactureService, BreakageAtion, Fault
from metro.models import Metro


class Proposal(models.Model):
  name = models.CharField(max_length=255)

  number = models.CharField(max_length=255)
  status = models.IntegerField()
  device_type = models.ForeignKey(
      DeviceType, null=True, on_delete=models.SET_NULL)
  brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
  device_model = models.ForeignKey(
      DeviceModel, null=True, on_delete=models.SET_NULL)
  fault = models.ForeignKey(
      Fault, null=True, on_delete=models.SET_NULL, blank=True)
  metro = models.ForeignKey(
      Metro, null=True, on_delete=models.SET_NULL, blank=True)

  date = models.DateTimeField(default=timezone.now())

  def __str__(self):
    return self.name

    class Meta:
        ordering = ['-date']
