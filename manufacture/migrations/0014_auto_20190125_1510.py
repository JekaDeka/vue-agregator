# Generated by Django 2.1.5 on 2019-01-25 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacture', '0013_auto_20190124_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacture',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]