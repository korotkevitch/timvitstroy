from django.contrib import admin


from home.models import Head
class HeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_1_preview', 'image_2_preview')
    list_display_links = ('id', 'title')
admin.site.register(Head, HeadAdmin)


from home.models import About
from home.forms import AboutForm
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'text', 'image_preview')
    form = AboutForm
    list_display_links = ('id', 'title')
admin.site.register(About, AboutAdmin)


from home.models import Service
from home.forms import ServiceForm
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_image_1_preview', 'service_title', 'service_text', 'link_text', 'title', 'subtitle', 'text')
    form = ServiceForm
    list_display_links = ('id', 'service_image_1_preview')
admin.site.register(Service, ServiceAdmin)


from .models import Testimonial
from home.forms import TestimonialForm
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'testimonial', 'image_preview')
    form = TestimonialForm
    list_display_links = ('id', 'name')
admin.site.register(Testimonial, TestimonialAdmin)

