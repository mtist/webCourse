# Generated by Django 2.0.2 on 2018-02-22 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='surname',
            field=models.CharField(max_length=30, verbose_name='Фамилия'),
        ),
    ]