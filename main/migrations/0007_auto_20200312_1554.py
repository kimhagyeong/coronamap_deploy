# Generated by Django 3.0.4 on 2020-03-12 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200312_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mask',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='mask',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]