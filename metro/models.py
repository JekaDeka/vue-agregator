from django.db import models


class Country(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name


class Town(models.Model):
  name = models.CharField(max_length=255)
  country = models.ForeignKey(
      Country, models.CASCADE, blank=True, null=True)

  def __str__(self):
    return self.name


class Metro(models.Model):
  name = models.CharField(max_length=255)
  town = models.ForeignKey(
      Town, models.CASCADE, blank=True, null=True)
  location = models.CharField(max_length=255)  # GeoIP()

  def __str__(self):
    return self.name
# Create your models here.
