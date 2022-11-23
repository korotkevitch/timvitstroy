from django.urls import path
from home import views
from .views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]