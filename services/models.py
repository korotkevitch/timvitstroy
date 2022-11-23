from django.db import models
from django.shortcuts import reverse
from django.utils.safestring import mark_safe


class ServicePage(models.Model):
    banner = models.FileField('Баннер в шапке 1600*235', upload_to='banners', blank=True)
    title = models.CharField('Заголовок раздела', max_length=50, blank=True)
    subtitle = models.CharField('Подзаголовок раздела', max_length=50, blank=True)
    text = models.CharField('Текст', max_length=1000, blank=True)
    image = models.FileField('Фото 880*548', upload_to='services', blank=True)
    bottom_title = models.CharField('Заголовок ниженго блока', max_length=50, blank=True)
    bottom_text = models.CharField('Текст ниженго блока', max_length=2000, blank=True)

    def banner_preview(self):
        if self.banner:
            return mark_safe('<img src="%s" style="width:100px; height:30px;" />' % self.banner.url)
        else:
            return 'No Image Found'

    banner_preview.short_description = 'Баннер в шапке'

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = 'Раздел "Услуги"'
        verbose_name_plural ='Раздел "Услуги"'

    def __str__(self):
        return self.title


class ServiceDetail(models.Model):
    banner = models.FileField('Баннер в шапке 1600*235', upload_to='banners', blank=True)
    name = models.CharField('Услуга', max_length=50, blank=True)
    slug = models.SlugField(max_length=80, unique=True)
    icon_1 = models.FileField('Иконка цветная 81*80', upload_to='icons', blank=True)
    icon_2 = models.FileField('Иконка белая 81*80', upload_to='icons', blank=True)
    short_description = models.CharField('Краткое описание', max_length=125, blank=True)
    title_1 = models.CharField('Название первого текста', max_length=50, blank=True)
    text_1 = models.CharField('Первый текст', max_length=2000, blank=True)
    title_2 = models.CharField('Название второго текста', max_length=50, blank=True)
    text_2 = models.CharField('Второй текст', max_length=2000, blank=True)
    image_1 = models.FileField('Фото 1, 1110*534', upload_to='services', blank=True)
    thumb_1 = models.FileField('Эскиз 1, 177*107', upload_to='services', blank=True)
    image_2 = models.FileField('Фото 2, 1110*534', upload_to='services', blank=True)
    thumb_2 = models.FileField('Эскиз 2, 177*107', upload_to='services', blank=True)
    image_3 = models.FileField('Фото 3, 1110*534', upload_to='services', blank=True)
    thumb_3 = models.FileField('Эскиз 3, 177*107', upload_to='services', blank=True)
    image_4 = models.FileField('Фото 4, 1110*534', upload_to='services', blank=True)
    thumb_4 = models.FileField('Эскиз 4, 177*107', upload_to='services', blank=True)
    image_5 = models.FileField('Фото 5, 1110*534', upload_to='services', blank=True)
    thumb_5 = models.FileField('Эскиз 5, 177*107', upload_to='services', blank=True)
    image_6 = models.FileField('Фото 6, 1110*534', upload_to='services', blank=True)
    thumb_6 = models.FileField('Эскиз 6, 177*107', upload_to='services', blank=True)
    image_7 = models.FileField('Фото 7, 1110*534', upload_to='services', blank=True)
    thumb_7 = models.FileField('Эскиз 7, 177*107', upload_to='services', blank=True)
    image_8 = models.FileField('Фото 8, 1110*534', upload_to='services', blank=True)
    thumb_8 = models.FileField('Эскиз 8, 177*107', upload_to='services', blank=True)
    image_9 = models.FileField('Фото 9, 1110*534', upload_to='services', blank=True)
    thumb_9 = models.FileField('Эскиз 9, 177*107', upload_to='services', blank=True)
    image_10 = models.FileField('Фото 10, 1110*534', upload_to='services', blank=True)
    thumb_10 = models.FileField('Эскиз 10, 177*107', upload_to='services', blank=True)

    def get_url(self):
        return reverse('service_details', args=[self.slug])

    def text_1_trim(self):
        return self.text_1[:100]
    text_1_trim.short_description = "Первый текст"

    def text_2_trim(self):
        return self.text_2[:100]
    text_2_trim.short_description = "Второй текст"

    def banner_preview(self):
        if self.banner:
            return mark_safe('<img src="%s" style="width:100px; height:30px;" />' % self.banner.url)
        else:
            return 'No Image Found'

    banner_preview.short_description = 'Баннер в шапке'

    def icon_1_preview(self):
        if self.icon_1:
            return mark_safe('<img src="%s" style="width:50px; height:50px;" />' % self.icon_1.url)
        else:
            return 'No Image Found'

    icon_1_preview.short_description = 'Иконка'

    def image_1_preview(self):
        if self.image_1:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image_1.url)
        else:
            return 'No Image Found'

    image_1_preview.short_description = 'Фото 1'

    def image_2_preview(self):
        if self.image_2:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image_2.url)
        else:
            return 'No Image Found'

    image_2_preview.short_description = 'Фото 2'

    def image_3_preview(self):
        if self.image_3:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image_3.url)
        else:
            return 'No Image Found'

    image_3_preview.short_description = 'Фото 3'

    def image_4_preview(self):
        if self.image_4:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image_4.url)
        else:
            return 'No Image Found'

    image_4_preview.short_description = 'Фото 4'

    def image_5_preview(self):
        if self.image_5:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image_5.url)
        else:
            return 'No Image Found'

    image_5_preview.short_description = 'Фото 5'

    def image_6_preview(self):
        if self.image_6:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image_6.url)
        else:
            return 'No Image Found'

    image_6_preview.short_description = 'Фото 6'

    def image_7_preview(self):
        if self.image_7:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image_7.url)
        else:
            return 'No Image Found'

    image_7_preview.short_description = 'Фото 7'

    def image_8_preview(self):
        if self.image_8:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image_8.url)
        else:
            return 'No Image Found'

    image_8_preview.short_description = 'Фото 8'

    def image_9_preview(self):
        if self.image_9:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image_9.url)
        else:
            return 'No Image Found'

    image_9_preview.short_description = 'Фото 9'

    def image_10_preview(self):
        if self.image_10:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image_10.url)
        else:
            return 'No Image Found'

    image_10_preview.short_description = 'Фото 10'

    class Meta:
        verbose_name = 'Подробности об услуге'
        verbose_name_plural ='Подробности об услугах'

    def __str__(self):
        return self.name