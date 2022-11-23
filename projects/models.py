from django.db import models
from django.shortcuts import reverse
from django.utils.safestring import mark_safe


class ProjectSection(models.Model):
    section = models.CharField('Категория', max_length=50, blank=True)
    alias = models.CharField('alias', max_length=50, blank=True)
    slug = models.SlugField(max_length=100, unique=True, default="")

    def get_url(self):
        return reverse('project_details', args=[self.slug])

    class Meta:
        verbose_name = 'Категория проекта'
        verbose_name_plural = 'Категории проектов'

    def __str__(self):
        return self.section


class IndProjectPage(models.Model):
    banner = models.FileField('Баннер в шапке 1600*235', upload_to='banners', blank=True)
    title = models.CharField('Заголовок раздела', max_length=50, blank=True)
    subtitle = models.CharField('Подзаголовок раздела', max_length=50, blank=True)
    text_title = models.CharField('Заголовок', max_length=50, blank=True)
    text = models.CharField('Текст', max_length=2000, blank=True)
    image = models.FileField('Фото', upload_to='ind_projects', blank=True)

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

    def article_trim(self):
        return self.article_text[:100]

    image_preview.short_description = 'Изображение'

    class Meta:
        verbose_name = 'Раздел "Проекты"'
        verbose_name_plural = 'Раздел "Проекты"'

    def __str__(self):
        return self.title


class ProjectPage(models.Model):
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
        verbose_name = 'Раздел "Проекты"'
        verbose_name_plural = 'Раздел "Проекты"'

    def __str__(self):
        return self.title


class ProjectDetail(models.Model):
    section = models.ForeignKey(ProjectSection, on_delete=models.CASCADE, default="", verbose_name='Секция')
    image = models.FileField('Фото для входа в проект 275*275', upload_to='projects', blank=True)
    name = models.CharField('Название проекта', max_length=100, blank=True)
    description = models.CharField(' Краткое описание', max_length=100, blank=True)
    article_photo = models.FileField('Фото в статье 730*460', upload_to='projects', blank=True)
    article_thumb = models.FileField('Эскиз фото в статье 277*139', upload_to='projects', blank=True)
    article_name = models.CharField('Название статьи', max_length=100, blank=True)
    article_text = models.CharField('Текст статьи', max_length=2000, blank=True)
    slug = models.SlugField(max_length=100, unique=True, default="")

    def get_url(self):
        return reverse('project_details', kwargs={'section_slug': self.section.slug, 'project_slug': self.slug })

    def prefix(self):
        return self.section.alias

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:70px; height:70px;" />' % self.image.url)
        else:
            return 'No Image Found'

    def article_trim(self):
        return self.article_text[:100]

    image_preview.short_description = 'Изображение'

    def article_photo_preview(self):
        if self.article_photo:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.article_photo.url)
        else:
            return 'No Image Found'

    article_photo_preview.short_description = 'Фото в статье'

    def article_thumb_preview(self):
        if self.article_thumb:
            return mark_safe('<img src="%s" style="width:100px; height:50px;" />' % self.article_thumb.url)
        else:
            return 'No Image Found'

    article_thumb_preview.short_description = 'Эскиз'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name