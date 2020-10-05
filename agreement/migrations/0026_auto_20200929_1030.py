# Generated by Django 3.0.3 on 2020-09-29 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreement', '0025_auto_20200929_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='number_of_owner',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='properties',
            name='property_size',
            field=models.IntegerField(help_text='size of the site in sft', max_length=100, null=True),
        ),
    ]