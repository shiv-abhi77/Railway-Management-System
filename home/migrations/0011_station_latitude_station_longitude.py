# Generated by Django 4.2.7 on 2023-11-08 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20180417_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='station',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]
