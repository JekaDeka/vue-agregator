# Generated by Django 2.1.4 on 2018-12-26 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manufacture_service', '0001_initial'),
        ('manufacture', '0001_initial'),
        ('device', '0002_sparepart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_client', models.CharField(max_length=255)),
                ('number_client', models.IntegerField()),
                ('status', models.IntegerField()),
                ('brand', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='device.Brand')),
                ('device_model', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='device.DeviceModel')),
                ('manufacture', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manufacture.Manufacture')),
                ('manufacture_service', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manufacture_service.ManufactureService')),
                ('mark', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='device.Mark')),
                ('master', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manufacture.Master')),
            ],
        ),
    ]