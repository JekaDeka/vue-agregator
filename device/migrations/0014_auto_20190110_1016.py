# Generated by Django 2.1.5 on 2019-01-10 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0013_auto_20190110_0456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devicemodel',
            old_name='type',
            new_name='type_device',
        ),
        migrations.RenameField(
            model_name='devicetype',
            old_name='device_afilication',
            new_name='device_affilication',
        ),
        migrations.AlterField(
            model_name='sparepart',
            name='mark',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='device.Mark'),
        ),
    ]
