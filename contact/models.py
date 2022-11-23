from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber
from django.utils import timezone
from django.core.exceptions import ValidationError


class Contact(models.Model):
    banner = models.FileField('Баннер в шапке 1600*235', upload_to='banners', blank=True)
    phone = models.CharField('Телефон', max_length=50, blank=True)
    address = models.CharField('Адрес', max_length=100, blank=True)
    viber = PhoneNumberField('Вайбер', null=False, blank=True, unique=True)
    email = models.EmailField('Email', max_length=50, blank=True)

    def phone_link(self):
        return PhoneNumber.from_string(phone_number=self.phone, region='RU').as_e164

    phone_link.short_description = 'Телефон для ссылки'

    def viber_link(self):
        number = str(self.viber)
        return number.replace('+', '')

    viber_link.short_description = 'Вайбер без +'

    def banner_preview(self):
        if self.banner:
            return mark_safe('<img src="%s" style="width:100px; height:30px;" />' % self.banner.url)
        else:
            return 'No Image Found'

    banner_preview.short_description = 'Баннер в шапке'

    class Meta:
        verbose_name = '       Контактные данные'
        verbose_name_plural = '       Контактные данные'

    def __str__(self):
        return "Телефоны"


def validate_file_extension(value):
  import os
  ext = os.path.splitext(value.name)[1]
  valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.jpeg']
  if not ext in valid_extensions:
    raise ValidationError('Формат файла запрещен к загрузке')
  else:
      return value


def validate_file_size(value):
  filesize = value.size

  if filesize > 5242880:
      raise ValidationError("Размер файла не должен превышать 5MB")
  else:
      return value


class ContactForm(models.Model):
    name = models.CharField('Имя', max_length=50, blank=True)
    email = models.EmailField('Емейл', max_length=50, blank=True)
    phone = models.CharField('Телефон', max_length=50, blank=True)
    message = models.TextField('Сообщение', max_length=500, blank=True)
    file = models.FileField('Баннер в шапке 1600*235', upload_to='uploads', blank=True, default="", validators=[validate_file_extension, validate_file_size])

    class Meta:
        verbose_name = 'Сообщение, заказ'
        verbose_name_plural = 'Сообщения, заказы'

    def __str__(self):
        return self.name