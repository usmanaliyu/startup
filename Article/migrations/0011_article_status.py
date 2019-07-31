# Generated by Django 2.2.2 on 2019-07-04 02:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0010_remove_article_status_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
