# Generated by Django 2.1.5 on 2019-01-10 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0015_auto_20190110_1038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devicemodel',
            old_name='type_device',
            new_name='device_type',
        ),
    ]