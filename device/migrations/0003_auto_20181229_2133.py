# Generated by Django 2.1.4 on 2018-12-29 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_sparepart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('series', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('translitor', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='static/device/img')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='devicemodel',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='devicemodel',
            name='device_type',
        ),
        migrations.RemoveField(
            model_name='devicemodel',
            name='img',
        ),
        migrations.RemoveField(
            model_name='devicemodel',
            name='mark',
        ),
        migrations.RemoveField(
            model_name='devicemodel',
            name='series',
        ),
        migrations.RemoveField(
            model_name='devicemodel',
            name='translitor',
        ),
        migrations.RemoveField(
            model_name='devicemodel',
            name='year',
        ),
        migrations.AddField(
            model_name='device',
            name='device_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.DeviceModel'),
        ),
        migrations.AddField(
            model_name='device',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.DeviceType'),
        ),
        migrations.AddField(
            model_name='device',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.Mark'),
        ),
    ]
