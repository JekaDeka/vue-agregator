from django.utils.translation import ugettext as _
from django.db.utils import IntegrityError
from django.core.management.base import CommandError

from pyexcel_xlsx import get_data
from device.models import Brand, DeviceType, DeviceModel, Mark, SparePart
from manufacture_service.models import BreakageAtion, Fault, ManufactureService
from django.core.management.base import BaseCommand
import json

DB_DEVICE_APPLE = 'Устройства'
DB_MANUFACTURE_SERVICE_APPLE = 'Услуги'
DB_FAULT_APPLE = 'Неисправности'
APPlE = 'Apple'


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

  for page in data:
    if(page == DB_DEVICE_APPLE):
      import_device_apple(data)
    if(page == DB_MANUFACTURE_SERVICE_APPLE):
      import_manufacture_service(data)
    if(page == DB_FAULT_APPLE):
      import_fault_apple(data)


def import_device_apple(data):
  brand = ''
  mark_object = ''
  try:
    brand = Brand.objects.get(name=APPlE)
  except Exception:
    brand = Brand.objects.create(name=APPlE)

  for device in data[DB_DEVICE_APPLE]:
    print(device)
    if len(device) == 5:
      if device[0] != '':
        name = device[0]
        translitor = device[4]
        try:
          mark_object = Mark.objects.get(name=name)
          mark_object.brand = brand
          mark_object.save()
        except Exception:
          mark_object = Mark.objects.create(name=name, translitor=translitor)
          mark_object.brand = brand
          mark_object.save()
          mark_object.save()
      elif device[1] != '':
        name = device[1]
        translitor = device[4]

        try:
          device_model_object = DeviceModel.objects.get(name=name)
          device_model_object.brand = brand
          device_model_object.mark = mark_object
          device_model_object.save()
        except Exception:
          device_model_object = DeviceModel.objects.create(
              name=name, translitor=translitor)
          device_model_object.brand = brand
          device_model_object.mark = mark_object
          device_model_object.save()
    elif len(device) == 6:
      name = ''
      series = device[3]
      translitor = device[3]
      year = device[5]
      if(device[1] != ''):
        name = device[1]
      else:
        name = device[2]
      try:
        device_model_object = DeviceModel.objects.get(name=name)
        device_model_object.series = series
        device_model_object.translitor = translitor
        device_model_object.year = year
        device_model_object.brand = brand
        device_model_object.mark = mark_object
        device_model_object.save()
      except Exception:

        print(name)

        device_model_object = DeviceModel.objects.create(name=name)
        device_model_object.series = series
        device_model_object.translitor = translitor
        device_model_object.year = year
        device_model_object.brand = brand
        device_model_object.mark = mark_object
        device_model_object.save()


def import_manufacture_service(data):
  mark_object = ''
  spare_part_object = ''
  try:
    brand = Brand.objects.get(name=APPlE)
  except Exception:
    brand = Brand.objects.create(name=APPlE)

  for device in data[DB_MANUFACTURE_SERVICE_APPLE]:
    if(len(device) == 1):
      name = device[0]
      try:
        mark_object = Mark.objects.get(name=name)
      except Exception:
        mark_object = Mark.objects.create(name=name)

    elif len(device) == 2:
      name = device[1]
      spare_part_object = SparePart.objects.create(name=name)
      spare_part_object.mark = mark_object
      spare_part_object.save()

    elif(len(device) != 0):
      name = device[2]

      spare_part_object = BreakageAtion.objects.create(name=name)
      spare_part_object.mark = mark_object
      spare_part_object.save()


def import_fault_apple(data):
  mark_object = ''
  spare_part_object = ''
  try:
    brand = Brand.objects.get(name=APPlE)
  except Exception:
    brand = Brand.objects.create(name=APPlE)
  for device in data[DB_FAULT_APPLE]:
    print(device)
    if(len(device) == 1):
      name = device[0]
      try:
        mark_object = Mark.objects.get(name=name)
      except Exception:
        mark_object = Mark.objects.create(name=name)
        mark_object.save()
    elif len(device) == 2:
      name = device[1]

      spare_part_object = SparePart.objects.create(name=name)
      spare_part_object.mark = mark_object
      spare_part_object.save()
    elif(len(device) != 0):
      name = device[2]
      translitor = device[3]
      actions = device[5:]
      fault_object = Fault.objects.create(name=name)
      fault_object.translitor = translitor
      fault_object.spare_part = spare_part_object
      fault_object.mark = mark_object
      fault_object.save()
      add_breakage_action(actions, mark_object, brand, fault_object)
      fault_object.save()


def add_breakage_action(actions, mark_object, brand, fault_object):
  breaking_action_object = ''
  for action in actions:

    breaking_action_object = BreakageAtion.objects.create(name=action)
    breaking_action_object.fault = fault_object
    breaking_action_object.mark = mark_object
    breaking_action_object.save()


def delete_db():
  Brand.objects.all().delete()
  Mark.objects.all().delete()
  DeviceType.objects.all().delete()
  DeviceModel.objects.all().delete()
  SparePart.objects.all().delete()
  ManufactureService.objects.all().delete()
  Fault.objects.all().delete()
  BreakageAtion.objects.all().delete()
