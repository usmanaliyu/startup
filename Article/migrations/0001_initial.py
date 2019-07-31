# Generated by Django 2.2.2 on 2019-07-02 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('summary', models.TextField(max_length=250)),
                ('title_body1', models.TextField(max_length=1000)),
                ('title_body2', models.TextField(max_length=1000)),
                ('title_body3', models.TextField(max_length=1000)),
                ('sub1', models.CharField(max_length=200)),
                ('sub1_child1', models.CharField(max_length=500)),
                ('sub1_child1_body', models.TextField(max_length=1000)),
                ('sub1_child2', models.CharField(max_length=500)),
                ('sub1_child2_body', models.TextField(max_length=1000)),
                ('sub1_child3', models.CharField(max_length=500)),
                ('sub1_child3_body', models.TextField(max_length=1000)),
                ('sub1_child4', models.CharField(max_length=500)),
                ('sub1_child4_body', models.TextField(max_length=1000)),
                ('sub1_child5', models.CharField(max_length=500)),
                ('sub1_child5_body', models.TextField(max_length=1000)),
                ('sub2', models.CharField(max_length=200)),
                ('sub2_child1', models.CharField(max_length=500)),
                ('sub2_child1_body', models.TextField(max_length=1000)),
                ('sub2_child2', models.CharField(max_length=500)),
                ('sub2_child2_body', models.TextField(max_length=1000)),
                ('sub2_child3', models.CharField(max_length=500)),
                ('sub2_child3_body', models.TextField(max_length=1000)),
                ('sub2_child4', models.CharField(max_length=500)),
                ('sub2_child4_body', models.TextField(max_length=1000)),
                ('sub2_child5', models.CharField(max_length=500)),
                ('sub2_child5_body', models.TextField(max_length=1000)),
                ('sub3', models.CharField(max_length=200)),
                ('sub3_child1', models.CharField(max_length=500)),
                ('sub3_child1_body', models.TextField(max_length=1000)),
                ('sub3_child2', models.CharField(max_length=500)),
                ('sub3_child2_body', models.TextField(max_length=1000)),
                ('sub3_child3', models.CharField(max_length=500)),
                ('sub3_child3_body', models.TextField(max_length=1000)),
                ('sub3_child4', models.CharField(max_length=500)),
                ('sub3_child4_body', models.TextField(max_length=1000)),
                ('sub3_child5', models.CharField(max_length=500)),
                ('sub3_child5_body', models.TextField(max_length=1000)),
                ('sub4', models.CharField(max_length=200)),
                ('sub4_child1', models.CharField(max_length=500)),
                ('sub4_child1_body', models.TextField(max_length=1000)),
                ('sub4_child2', models.CharField(max_length=500)),
                ('sub4_child2_body', models.TextField(max_length=1000)),
                ('sub4_child3', models.CharField(max_length=500)),
                ('sub4_child3_body', models.TextField(max_length=1000)),
                ('sub4_child4', models.CharField(max_length=500)),
                ('sub4_child4_body', models.TextField(max_length=1000)),
                ('sub4_child5', models.CharField(max_length=500)),
                ('sub4_child5_body', models.TextField(max_length=1000)),
                ('sub5', models.CharField(max_length=200)),
                ('sub5_child1', models.CharField(max_length=500)),
                ('sub5_child1_body', models.TextField(max_length=1000)),
                ('sub5_child2', models.CharField(max_length=500)),
                ('sub5_child2_body', models.TextField(max_length=1000)),
                ('sub5_child3', models.CharField(max_length=500)),
                ('sub5_child3_body', models.TextField(max_length=1000)),
                ('sub5_child4', models.CharField(max_length=500)),
                ('sub5_child4_body', models.TextField(max_length=1000)),
                ('sub5_child5', models.CharField(max_length=500)),
                ('sub5_child5_body', models.TextField(max_length=1000)),
            ],
        ),
    ]