from django.db import models


class DeviceAffiliation (models.Model):
  """
  Устройства поле
  """
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name


class DeviceType(models.Model):
  name = models.CharField(max_length=255)
  device_affilication = models.ForeignKey(
      DeviceAffiliation, on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
    return self.name


class Brand (models.Model):
  """
  Класс бренд
  примеры значения поля имени:
  name = Apple
  """
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name


class Mark(models.Model):
  """
  Класс марки
  пример значения поля имени:
  name = Iphone

  Весь основной поиск будет происходить в данном классе
  """

  brand = models.ForeignKey(
      Brand, on_delete=models.CASCADE, blank=True, null=True)
  name = models.CharField(max_length=255)
  translitor = models.CharField(max_length=255, blank=True, default='')

  def __str__(self):
    return self.name


class DeviceModel(models.Model):
  """
  Модель. Связнная с бренбом и маркой
  """

  name = models.CharField(max_length=255)
  series = models.CharField(max_length=255, blank=True, default='')
  year = models.CharField(max_length=255, blank=True,
                          default='')  # IntegerField(default=0)
  translitor = models.CharField(blank=True, max_length=255, default='')
  img = models.ImageField(upload_to='static/device/img', blank=True)

  device_type = models.ForeignKey(DeviceType, blank=True,
                                  on_delete=models.CASCADE, null=True)
  brand = models.ForeignKey(
      Brand, on_delete=models.CASCADE, blank=True, null=True)
  mark = models.ForeignKey(
      Mark, on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
    return self.name


class SparePart(models.Model):
  """
  Поломанная часть

  """
  name = models.CharField(max_length=255)
  mark = models.ForeignKey(
      Mark, on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
    return self.name
