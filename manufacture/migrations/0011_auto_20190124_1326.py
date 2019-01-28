# Generated by Django 2.1.5 on 2019-01-24 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacture', '0010_auto_20190124_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255)),
                ('multichannel', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='manufacture',
            name='des_ptr',
        ),
        migrations.RemoveField(
            model_name='manufacture',
            name='login',
        ),
        migrations.RemoveField(
            model_name='manufacture',
            name='password',
        ),
        migrations.RemoveField(
            model_name='master',
            name='login',
        ),
        migrations.RemoveField(
            model_name='master',
            name='password',
        ),
        migrations.AddField(
            model_name='manufacture',
            name='comment_courier',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='comment_diagnostic',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='courier',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='diagnostic',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manufacture',
            name='master_home',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='master_home_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='pay_card',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='urgent_repairs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='work_clock_saturday_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='work_clock_saturday_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='work_clock_suday_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='work_clock_sunday_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='work_clock_weekdays_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='work_clock_weekdays_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='master',
            name='comment_courier',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='master',
            name='comment_diagnostic',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='master',
            name='courier',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='master',
            name='diagnostic',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='master',
            name='master_home',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='master',
            name='master_home_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='master',
            name='pay_card',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='master',
            name='urgent_repairs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='master',
            name='work_clock_saturday_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='master',
            name='work_clock_saturday_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='master',
            name='work_clock_suday_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='master',
            name='work_clock_sunday_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='master',
            name='work_clock_weekdays_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='master',
            name='work_clock_weekdays_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.DeleteModel(
            name='Des',
        ),
        migrations.AddField(
            model_name='manufacture',
            name='number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manufacture.Number'),
        ),
        migrations.AddField(
            model_name='master',
            name='number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manufacture.Number'),
        ),
    ]
