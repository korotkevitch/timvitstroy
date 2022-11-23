from django import forms
# from captcha.fields import ReCaptchaField
from django.core.mail import send_mail as django_send_mail
from .models import ContactForm


class UserForm(forms.ModelForm):
    # captcha = ReCaptchaField(
    #     public_key='6LdbmQkeAAAAADPuywAjtXN4u-Pd31SfkXBUAHxm',
    #     private_key='6LdbmQkeAAAAAN2ZnJ3-PPe3VkZzScSbyd3AVjKm',
    # )

    class Meta:
        model = ContactForm
        fields = '__all__'  # вместо перечисления всех полей: fields = ['name', 'phone', 'message']

    def send_mail(self):
        return django_send_mail('Сообщение с сайта timvitstroy.by',
                    str('Имя: ') + self.cleaned_data['name'] + '\n' + str('Емейл: ') + self.cleaned_data['email'] + '\n' + str('Телефон: ') + self.cleaned_data['phone'] + '\n' + str('Сообщение: ') + self.cleaned_data['message'],
                    'no-reply@timvitstroy.by',
                    ['info@iko-studio.com'])


# from django import forms
# from django.core.exceptions import ValidationError
#
# from .models import *
#
# class AddPostForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['cat'].empty_label = "Категория не выбрана"
#
#     class Meta:
#         model = Women
#         fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-input'}),
#             'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
#         }
#
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         if len(title) > 200:
#             raise ValidationError('Длина превышает 200 символов')
#
#         return title
