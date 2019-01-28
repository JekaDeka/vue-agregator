# Generated by Django 2.1.5 on 2019-01-10 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0016_auto_20190110_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devicemodel',
            old_name='device_type',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='img',
        ),
        migrations.RemoveField(
            model_name='deviceaffiliation',
            name='img',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='img',
        ),
        migrations.AlterField(
            model_name='sparepart',
            name='mark',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.Mark'),
        ),
    ]