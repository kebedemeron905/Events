# Generated by Django 2.0.5 on 2018-05-31 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bachata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time_start',
            field=models.TimeField(),
        ),
    ]
