# Generated by Django 2.1.5 on 2019-01-10 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metro', '0003_metro_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metro',
            name='img',
        ),
    ]
