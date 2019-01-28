# Generated by Django 2.1.4 on 2018-12-30 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0004_auto_20181230_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicemodel',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.Brand'),
        ),
        migrations.AlterField(
            model_name='devicemodel',
            name='mark',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.Mark'),
        ),
        migrations.AlterField(
            model_name='devicemodel',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.DeviceType'),
        ),
    ]
