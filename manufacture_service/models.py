from django.db import models
from device.models import Mark, SparePart, Brand
from manufacture.models import Manufacture, Master


class Fault(models.Model):
  """
  Конкретная поломка/ неисправность
  """
  name = models.CharField(max_length=255)
  translitor = models.CharField(max_length=255)
  spare_part = models.ForeignKey(
      SparePart, models.CASCADE, blank=True, null=True)
  mark = models.ForeignKey(
      Mark, on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
    return self.name


class BreakageAtion(models.Model):
  """
  Действие по решению проблемы
  """
  name = models.CharField(max_length=255)
  link = models.URLField(max_length=255, blank=True, default='')

  fault = models.ForeignKey(
      Fault, on_delete=models.CASCADE, blank=True, null=True)
  mark = models.ForeignKey(
      Mark, blank=True, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.name


class ManufactureService(models.Model):
  """
  Услуга сервиса
  """
  mark = models.ForeignKey(
      Mark, blank=True, on_delete=models.CASCADE, null=True)

  manufacture = models.ForeignKey(
      Manufacture, on_delete=models.CASCADE, blank=True, null=True)
  master = models.ForeignKey(
      Master, on_delete=models.CASCADE, blank=True, null=True)

  breaking_action = models.ForeignKey(
      BreakageAtion, on_delete=models.CASCADE, blank=True, null=True)

  price = models.IntegerField(default=0)

  def __str__(self):
    return self.breaking_action.name

# Create your models here.
