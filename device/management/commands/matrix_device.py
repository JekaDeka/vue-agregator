from django.utils.translation import ugettext as _
from django.db.utils import IntegrityError
from django.core.management.base import CommandError

from pyexcel_xlsx import get_data
from device.models import Brand, DeviceType, DeviceModel, DeviceAffiliation
from django.core.management.base import BaseCommand
import json


class Command(BaseCommand):
  args = '--import/--export/--delete/--hello <csv_file>'
  help = _("The command for device database")

  def add_arguments(self, parser):
    parser.add_argument(
        '--import',
        action='store_true',
        dest='import',
        default=False,
        help=_('Import products from csv file.')
    )
    parser.add_argument(
        '--export',
        action='store_true',
        dest='export',
        default=False,
        help=_('Export products from csv file.'))
    parser.add_argument(
        '--hello',
        action='store_true',
        dest='hello',
        default=False,
        help=_('Print hello'))
    parser.add_argument(
        '--delete',
        action='store_true',
        dest='delete',
        default=False,
        help=_('Delete data base device'))
    parser.add_argument(
        nargs='+',
        type=str,
        dest='args'
    )

  def handle(self, *args, **options):
    try:
      xlxs_file = args[0]
    except IndexError:
      raise CommandError(_("Please provide xlxs file to import"))
    if options["import"] and options["export"] and options['delete']:
      raise CommandError("can't both import and export and delete")
    if not options["import"] and not options["export"] and not options['delete'] and not options['hello']:
      raise CommandError(_("Wrong argument"))
    if options['import']:
      xlxs_file = xlxs_file
      import_data(xlxs_file)
    elif options['delete']:
      delete_db()
    elif options['hello']:
      print('hello ' + xlxs_file)


def import_data(xlxs_file):
  data = get_data(xlxs_file)
  device_type_object = ''
  brand_object = ''

  for page in data:
    try:
      device_affilication = DeviceAffiliation.objects.get(name=page)
    except Exception:
      device_affilication = DeviceAffiliation.objects.create(name=page)
    i = 0
    for device in data[page]:

      if (i == 0):
        i += 1
        continue
      print(device)
      if(len(device) == 3):
        device_type = device[0]
        try:
          device_type_object = DeviceType.objects.get(name=device_type)
        except Exception:
          device_type_object = DeviceType.objects.create(name=device_type)
          device_type_object.device_affilication = device_affilication
          device_type_object.save()
        brand = device[1]
        try:
          brand_object = Brand.objects.get(name=brand)
        except Exception:
          brand_object = Brand.objects.create(name=brand)
          brand_object.save()
        name = device[2]
        print(name)
        try:
          device_model_object = DeviceModel.objects.get(name=name)
          device_model_object.device_type = device_type_object
          device_model_object.brand = brand_object
          device_model_object.save()

        except Exception:

          print(name)
          device_model_object = DeviceModel.objects.create(name=name)
          device_model_object.type = device_type_object
          device_model_object.brand = brand_object
          device_model_object.save()


def delete_db():
  DeviceAffiliation.objects.all().delete()
  Brand.objects.all().delete()
  DeviceType.objects.all().delete()
  DeviceModel.objects.all().delete()
