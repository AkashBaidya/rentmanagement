# Generated by Django 3.0.3 on 2020-08-18 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreement', '0008_auto_20200712_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='interest_rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='rentline',
            name='advance_agreement_per_month',
            field=models.IntegerField(null=True),
        ),
    ]
