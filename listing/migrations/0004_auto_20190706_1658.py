# Generated by Django 2.2.2 on 2019-07-06 16:58

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0003_auto_20190706_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
