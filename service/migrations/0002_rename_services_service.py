# Generated by Django 5.1.3 on 2025-01-17 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
    ]
