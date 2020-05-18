# Generated by Django 3.0.3 on 2020-03-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='shop',
            new_name='branch_manager',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='purchase_date',
            new_name='entry_date',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='brand',
            new_name='site_type',
        ),
        migrations.RemoveField(
            model_name='site',
            name='address',
        ),
        migrations.RemoveField(
            model_name='site',
            name='model_code',
        ),
        migrations.RemoveField(
            model_name='site',
            name='quantity',
        ),
        migrations.AddField(
            model_name='site',
            name='comments',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]
