# Generated by Django 4.0.1 on 2022-02-03 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_projectsection_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectdetail',
            name='prefix',
        ),
    ]