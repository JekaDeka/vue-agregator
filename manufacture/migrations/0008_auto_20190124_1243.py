# Generated by Django 2.1.5 on 2019-01-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacture', '0007_auto_20190118_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacture',
            name='login',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manufacture',
            name='password',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='master',
            name='login',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='master',
            name='password',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
