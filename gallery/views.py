from django.shortcuts import render
from django.views.generic import View, ListView
from .models import GalleryPage, GalleryDetail

class GalleryPageView(ListView):
    model = GalleryPage
    template_name = 'gallery.html'
    context_object_name = 'page_gallery'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['all_photos'] = GalleryDetail.objects.all()
        return context
