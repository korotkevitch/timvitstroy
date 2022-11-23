from django.db import models
from django.utils.safestring import mark_safe


class Head(models.Model):
    title = models.CharField('Title страницы', max_length=120, blank=True)
    image_1 = models.FileField('Первый слайд 1920*1280', upload_to='home', blank=True)
    image_2 = models.FileField('Второй слайд 1920*1280', upload_to='home', blank=True)

    def image_1_preview(self):
        if self.image_1:
            return mark_safe('<img src="%s" style="width:100px; height:60px;" />' % self.image_1.url)
        else:
            return 'No Image Found'

    image_1_preview.short_description = 'Первый слайд'

    def image_2_preview(self):
        if self.image_2:
            return mark_safe('<img src="%s" style="width:100px; height:60px;" />' % self.image_2.url)
        else:
            return 'No Image Found'

    image_2_preview.short_description = 'Второй слайд'

    class Meta:
        verbose_name = '       Верхняя часть с фото'
        verbose_name_plural ='       Верхняя часть с фото'

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField('Заголовок', max_length=50, blank=True)
    subtitle = models.CharField('Подзаголовок', max_length=50, blank=True)
    text = models.CharField('Текст', max_length=750, blank=True)
    image = models.FileField('Изображение 660*600', upload_to='home', blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:90px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = 'Кратко о нас'
        verbose_name_plural ='Кратко о нас'

    def __str__(self):
        return self.title


class Service(models.Model):
    service_image_1 = models.FileField('Иконка цветная 48*48', upload_to='icons', blank=True)
    service_image_2 = models.FileField('Иконка белая 48*48', upload_to='icons', blank=True)
    service_title = models.CharField('Название услуги', max_length=50, blank=True)
    service_text = models.CharField('О сервисе', max_length=100, blank=True)
    link_text = models.CharField('Текст ссылки', max_length=20, blank=True)
    title = models.CharField('Заголовок раздела', max_length=50, blank=True)
    subtitle = models.CharField('Подзаголовок раздела', max_length=70, blank=True)
    text = models.CharField('Текст раздела', max_length=750, blank=True)

    def service_image_1_preview(self):
        if self.service_image_1:
            return mark_safe('<img src="%s" style="width:48px; height:48px;" />' % self.service_image_1.url)
        else:
            return 'No Image Found'

    service_image_1_preview.short_description = 'Иконка 1'

    def service_image_2_preview(self):
        if self.service_image_2:
            return mark_safe('<img src="%s" style="width:48px; height:48px;" />' % self.service_image_2.url)
        else:
            return 'No Image Found'

    service_image_2_preview.short_description = 'Иконка 2'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural ='Услуги'

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField('Имя, фамилия', max_length=50, blank=True)
    testimonial = models.CharField('Отзыв', max_length=800, blank=True)
    image = models.FileField('Картинка 160*205', upload_to='home',blank=True)


    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:80px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото человека'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name