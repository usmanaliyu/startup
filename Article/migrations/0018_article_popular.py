# Generated by Django 2.2.2 on 2019-07-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0017_delete_attendee'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='popular',
            field=models.CharField(blank=True, choices=[('true', 'True'), ('false', 'False')], max_length=50),
        ),
    ]
