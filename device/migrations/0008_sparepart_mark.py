# Generated by Django 2.1.4 on 2019-01-01 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0007_auto_20181230_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparepart',
            name='mark',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='device.Mark'),
            preserve_default=False,
        ),
    ]
