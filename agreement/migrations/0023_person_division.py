# Generated by Django 3.0.3 on 2020-09-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreement', '0022_auto_20200929_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='division',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
