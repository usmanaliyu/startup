# Generated by Django 2.2.2 on 2001-01-01 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0013_auto_20010101_0019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='segment',
            new_name='category',
        ),
    ]