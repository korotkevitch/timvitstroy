# Generated by Django 4.0.1 on 2022-02-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projectdetail_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdetail',
            name='prefix',
            field=models.CharField(blank=True, max_length=3, verbose_name='Префикс для фильтра'),
        ),
    ]
