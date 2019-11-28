# Generated by Django 2.2.2 on 2019-11-25 13:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogue',
            name='is_shared',
            field=models.BooleanField(default=False, verbose_name='是否已经分享'),
        ),
        migrations.AddField(
            model_name='myfile',
            name='reference_count',
            field=models.IntegerField(default=0, verbose_name='引用次数'),
        ),
        migrations.AlterField(
            model_name='myfile',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
    ]
