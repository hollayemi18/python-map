# Generated by Django 3.2.2 on 2023-05-31 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_id_address_store'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='store',
            new_name='id',
        ),
    ]
