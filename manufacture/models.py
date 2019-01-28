from django.db import models
from metro.models import Metro, Town, Country
# from django.contrib.gis.geoip import GeoIP


class User(models.Model):
  login = models.CharField(max_length=255)
  password = models.CharField(max_length=255)

  class Meta:
    abstract = True


class Description():
  pass

  class Meta:
    abstract = True


class Descript(models.Model):
  name = models.CharField(max_length=255)
  content = models.TextField(blank=True, null=True)
  adress = models.CharField(max_length=255, blank=True, null=True)
  country = models.ForeignKey(
      Country, blank=True, on_delete=models.SET_NULL, null=True)
  town = models.ForeignKey(
      Town, blank=True, on_delete=models.SET_NULL, null=True)
  metro = models.ManyToManyField(
      Metro, blank=True, null=True, default=[])
  how_search = models.TextField(blank=True, null=True)
  how_get = models.TextField(blank=True, null=True)

  class Meta:
    abstract = True


class ContactInformation(models.Model):
  work_clock_weekdays_start = models.TimeField(null=True)
  work_clock_weekdays_end = models.TimeField(null=True)
  work_clock_saturday_start = models.TimeField(null=True)
  work_clock_saturday_end = models.TimeField(null=True)
  work_clock_sunday_start = models.TimeField(null=True)
  work_clock_sunday_end = models.TimeField(null=True)
  comment_time_work = models.TextField(blank=True, default='')

  class Meta:
    abstract = True


class Options(models.Model):
  pay_card = models.BooleanField(default=False)
  courier = models.BooleanField(default=False)
  comment_courier = models.TextField(blank=True, null=True)
  diagnostic = models.BooleanField(default=False)
  comment_diagnostic = models.TextField(blank=True, null=True)
  master_home = models.BooleanField(default=False)
  master_home_comment = models.TextField(blank=True, null=True)

  urgent_repairs = models.BooleanField(default=False)

  class Meta:
    abstract = True


class Manufacture(Descript, ContactInformation, Options, User):
  office = models.CharField(max_length=255, blank=True, default='')
  link = models.URLField(blank=True, null=True)

  class Meta:
    abstract = False


class Master(Descript, ContactInformation, Options, User):
  is_private = models.BooleanField(default=True)
  manufacture = models.ForeignKey(
      Manufacture, blank=True, on_delete=models.CASCADE, null=True)

  class Meta:
    abstract = False


class Number(models.Model):
  number = models.CharField(max_length=255)
  multichannel = models.BooleanField(default=False)
  manufacture = models.ForeignKey(
      Manufacture, on_delete=models.CASCADE, blank=True, null=True)
  master = models.ForeignKey(
      Master, on_delete=models.CASCADE, blank=True, null=True)

  def _str__(self):
    return self.number


# Create your models here.
