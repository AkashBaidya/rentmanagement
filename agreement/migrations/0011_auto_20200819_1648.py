# Generated by Django 3.0.3 on 2020-08-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreement', '0010_auto_20200819_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='agrement_advance_amount',
            field=models.DecimalField(decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='agrement_security_amount',
            field=models.DecimalField(decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='interest_rate',
            field=models.DecimalField(decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='rentline',
            name='advance_agreement_per_month',
            field=models.DecimalField(decimal_places=4, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='rentline',
            name='rent_per_month',
            field=models.DecimalField(decimal_places=4, max_digits=30, null=True),
        ),
    ]
