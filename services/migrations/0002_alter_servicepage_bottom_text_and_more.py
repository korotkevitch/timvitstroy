# Generated by Django 4.0.1 on 2022-01-28 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepage',
            name='bottom_text',
            field=models.CharField(blank=True, max_length=2000, verbose_name='Текст ниженго блока'),
        ),
        migrations.AlterField(
            model_name='servicepage',
            name='service_text',
            field=models.CharField(blank=True, max_length=250, verbose_name='Описание услуги'),
        ),
        migrations.AlterField(
            model_name='servicepage',
            name='text',
            field=models.CharField(blank=True, max_length=450, verbose_name='Текст'),
        ),
    ]