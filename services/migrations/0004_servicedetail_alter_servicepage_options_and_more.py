# Generated by Django 4.0.1 on 2022-01-29 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_servicepage_service_image_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_image_1', models.FileField(blank=True, upload_to='', verbose_name='Изображение 1')),
                ('service_image_2', models.FileField(blank=True, upload_to='', verbose_name='Изображение 2')),
                ('service_title', models.CharField(blank=True, max_length=50, verbose_name='Название услуги')),
                ('service_text', models.CharField(blank=True, max_length=250, verbose_name='Описание услуги')),
            ],
            options={
                'verbose_name': 'Подробности об услуге',
                'verbose_name_plural': 'Подробности об услугах',
            },
        ),
        migrations.AlterModelOptions(
            name='servicepage',
            options={'verbose_name': 'Раздел "Услуги"', 'verbose_name_plural': 'Раздел "Услуги"'},
        ),
        migrations.RemoveField(
            model_name='servicepage',
            name='service_image_1',
        ),
        migrations.RemoveField(
            model_name='servicepage',
            name='service_image_2',
        ),
        migrations.RemoveField(
            model_name='servicepage',
            name='service_text',
        ),
        migrations.RemoveField(
            model_name='servicepage',
            name='service_title',
        ),
    ]
