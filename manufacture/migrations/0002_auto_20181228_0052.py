# Generated by Django 2.1.4 on 2018-12-28 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metro', '0002_metro_location'),
        ('manufacture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacture',
            name='location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='metro',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='metro.Metro'),
        ),
        migrations.AddField(
            model_name='master',
            name='location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='master',
            name='metro',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='metro.Metro'),
        ),
    ]
