# Generated by Django 4.0.1 on 2022-02-09 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_indprojectpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='indprojectpage',
            name='image',
            field=models.FileField(blank=True, upload_to='ind_projects', verbose_name='Фото'),
        ),
    ]