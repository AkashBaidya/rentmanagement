# Generated by Django 3.0.3 on 2020-09-28 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agreement', '0016_auto_20200928_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='Area',
            new_name='area',
        ),
    ]
