# Generated by Django 2.1.4 on 2019-01-01 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0009_remove_sparepart_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparepart',
            name='mark',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='device.Mark'),
        ),
    ]