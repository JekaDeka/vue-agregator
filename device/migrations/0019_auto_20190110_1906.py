# Generated by Django 2.1.5 on 2019-01-10 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0018_brand_device_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devicemodel',
            old_name='type',
            new_name='device_type',
        ),
    ]
