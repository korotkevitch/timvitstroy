from django.contrib import admin


from services.models import ServicePage
from home.forms import ServicePageForm
class ServicePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'banner_preview', 'text', 'image_preview', 'bottom_title', 'bottom_text')
    form = ServicePageForm
    list_display_links = ('id', 'title')
admin.site.register(ServicePage, ServicePageAdmin)


from services.models import ServiceDetail
class ServiceDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon_1_preview', 'short_description', 'banner_preview', 'title_1', 'text_1_trim', 'title_2', 'text_2_trim',
                    'slug', 'image_1_preview', 'image_2_preview', 'image_3_preview', 'image_4_preview', 'image_5_preview',
                    'image_6_preview', 'image_7_preview', 'image_8_preview', 'image_9_preview', 'image_10_preview')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(ServiceDetail, ServiceDetailAdmin)
