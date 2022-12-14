# Generated by Django 4.0.1 on 2022-02-08 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_alter_projectdetail_image_alter_projectpage_banner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetail',
            name='article_photo',
            field=models.FileField(blank=True, upload_to='projects', verbose_name='Фото в статье 730*460'),
        ),
        migrations.AlterField(
            model_name='projectdetail',
            name='article_thumb',
            field=models.FileField(blank=True, upload_to='projects', verbose_name='Эскиз фото в статье 277*139'),
        ),
        migrations.AlterField(
            model_name='projectdetail',
            name='image',
            field=models.FileField(blank=True, upload_to='projects', verbose_name='Фото для входа в проект 275*275'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='banner',
            field=models.FileField(blank=True, upload_to='banners', verbose_name='Баннер в шапке 1600*235'),
        ),
    ]
