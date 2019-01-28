# Generated by Django 2.1.5 on 2019-01-10 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacture', '0002_auto_20181228_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacture',
            name='metro',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='metro.Metro'),
        ),
        migrations.AlterField(
            model_name='master',
            name='manufacture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manufacture.Manufacture'),
        ),
        migrations.AlterField(
            model_name='master',
            name='metro',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='metro.Metro'),
        ),
    ]
