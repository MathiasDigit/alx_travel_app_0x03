# Generated by Django 5.2.1 on 2025-07-20 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='property',
            new_name='listing',
        ),
    ]
