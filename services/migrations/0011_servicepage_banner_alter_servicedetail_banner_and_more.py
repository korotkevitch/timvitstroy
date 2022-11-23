# Generated by Django 4.0.1 on 2022-02-08 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_alter_servicedetail_banner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepage',
            name='banner',
            field=models.FileField(blank=True, upload_to='banners', verbose_name='Баннер в шапке 1600*235'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='banner',
            field=models.FileField(blank=True, upload_to='banners', verbose_name='Баннер в шапке 1600*235'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='icon_1',
            field=models.FileField(blank=True, upload_to='icons', verbose_name='Иконка цветная 81*80'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='icon_2',
            field=models.FileField(blank=True, upload_to='icons', verbose_name='Иконка белая 81*80'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='image_1',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Фото 1, 1110*534'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='image_10',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Фото 10, 1110*534'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='image_2',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Фото 2, 1110*534'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='image_3',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Фото 3, 1110*534'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='image_4',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Фото 4, 1110*534'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='image_5',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Фото 5, 1110*534'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='image_6',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Фото 6, 1110*534'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='image_7',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Фото 7, 1110*534'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='image_8',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Фото 8, 1110*534'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='image_9',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Фото 9, 1110*534'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='thumb_1',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Эскиз 1, 177*107'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='thumb_10',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Эскиз 10, 177*107'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='thumb_2',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Эскиз 2, 177*107'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='thumb_3',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Эскиз 3, 177*107'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='thumb_4',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Эскиз 4, 177*107'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='thumb_5',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Эскиз 5, 177*107'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='thumb_6',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Эскиз 6, 177*107'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='thumb_7',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Эскиз 7, 177*107'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='thumb_8',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Эскиз 8, 177*107'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='thumb_9',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Эскиз 9, 177*107'),
        ),
        migrations.AlterField(
            model_name='servicepage',
            name='image',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Фото 880*548'),
        ),
    ]