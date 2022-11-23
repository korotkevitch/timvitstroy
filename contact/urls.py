from django.urls import path
from contact import views
from .views import ContactFormView
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='contacts.html')),
]