# Generated by Django 2.1.4 on 2019-01-01 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacture_service', '0003_auto_20190101_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakageation',
            name='fault',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manufacture_service.Fault'),
        ),
        migrations.AlterField(
            model_name='breakageation',
            name='manufacture_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manufacture_service.ManufactureService'),
        ),
        migrations.AlterField(
            model_name='breakageation',
            name='mark',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.Mark'),
        ),
        migrations.AlterField(
            model_name='fault',
            name='mark',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.Mark'),
        ),
        migrations.AlterField(
            model_name='fault',
            name='spare_part',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.SparePart'),
        ),
    ]
