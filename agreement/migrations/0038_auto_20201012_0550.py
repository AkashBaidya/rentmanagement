# Generated by Django 3.0.3 on 2020-10-12 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreement', '0037_auto_20201009_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='agreement_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='agrm_id',
            field=models.CharField(blank=True, default='hello', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='effected_date_as_actual',
            field=models.DateField(blank=True, null=True, verbose_name='Effective date as actual'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='effected_date_as_per_agreement',
            field=models.DateField(blank=True, null=True, verbose_name='Effective date as per agreement'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='expiry_date',
            field=models.DateField(blank=True, null=True, verbose_name='Expiry date'),
        ),
        migrations.AlterField(
            model_name='person',
            name='hasbankinfo',
            field=models.CharField(max_length=50, verbose_name='Bank account numnber'),
        ),
    ]
