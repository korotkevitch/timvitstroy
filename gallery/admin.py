from django.contrib import admin


from gallery.models import GalleryPage
from home.forms import GalleryPageForm
class GalleryPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'bottom_title', 'bottom_text', 'banner_preview')
    form = GalleryPageForm
    list_display_links = ('id', 'title')
admin.site.register(GalleryPage, GalleryPageAdmin)


from gallery.models import GalleryDetail
class GalleryDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'image_title', 'thumb_preview')
    list_display_links = ('id', 'image_preview')
admin.site.register(GalleryDetail, GalleryDetailAdmin)
