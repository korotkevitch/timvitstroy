# Generated by Django 4.0.1 on 2022-02-05 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_alter_projectdetail_article_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetail',
            name='image',
            field=models.FileField(blank=True, upload_to='', verbose_name='Фото для входа в проект 275*275'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='banner',
            field=models.FileField(blank=True, upload_to='', verbose_name='Баннер в шапке 1600*235'),
        ),
        migrations.AlterField(
            model_name='projectsection',
            name='alias',
            field=models.CharField(blank=True, max_length=50, verbose_name='alias'),
        ),
        migrations.AlterField(
            model_name='projectsection',
            name='section',
            field=models.CharField(blank=True, max_length=50, verbose_name='Категория'),
        ),
    ]
