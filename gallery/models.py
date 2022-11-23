from django.db import models
from django.shortcuts import reverse
from django.utils.safestring import mark_safe


class GalleryPage(models.Model):
    banner = models.FileField('Баннер в шапке 1600*235', upload_to='banners', blank=True)
    title = models.CharField('Заголовок раздела', max_length=50, blank=True)
    subtitle = models.CharField('Подзаголовок раздела', max_length=50, blank=True)
    bottom_title = models.CharField('Заголовок ниженго блока', max_length=50, blank=True)
    bottom_text = models.CharField('Текст ниженго блока', max_length=2000, blank=True)

    def banner_preview(self):
        if self.banner:
            return mark_safe('<img src="%s" style="width:100px; height:30px;" />' % self.banner.url)
        else:
            return 'No Image Found'

    banner_preview.short_description = 'Баннер в шапке'

    class Meta:
        verbose_name = 'Раздел "Галерея"'
        verbose_name_plural ='Раздел "Галерея"'

    def __str__(self):
        return self.title


class GalleryDetail(models.Model):
    image = models.FileField('Фото, 1110*534', upload_to='gallery', blank=True)
    image_title = models.CharField('Подпись к фото', max_length=100, blank=True)
    thumb = models.FileField('Эскиз, 177*107', upload_to='gallery', blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:60px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото'

    def thumb_preview(self):
        if self.thumb:
            return mark_safe('<img src="%s" style="width:100px; height:60px;" />' % self.thumb.url)
        else:
            return 'No Image Found'

    thumb_preview.short_description = 'Эскиз'

    class Meta:
        verbose_name = 'Фото галереи'
        verbose_name_plural ='Фото галереи'

    def __str__(self):
        return "Галерея"
