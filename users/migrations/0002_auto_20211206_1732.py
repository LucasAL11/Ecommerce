# Generated by Django 3.2.9 on 2021-12-06 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='address',
            field=models.CharField(blank=True, max_length=20, verbose_name='adress'),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='Phone number'),
        ),
    ]
