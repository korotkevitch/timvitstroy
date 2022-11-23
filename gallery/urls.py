from django.urls import path
from .views import GalleryPageView


urlpatterns = [
    path('', GalleryPageView.as_view(), name='gallery'),
]