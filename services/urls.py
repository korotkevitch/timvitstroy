from django.urls import path
from home import views
from django.views.generic import TemplateView
from .views import ServicePageView, ServiceDetailView


urlpatterns = [
    path('', ServicePageView.as_view(), name='services'),
    path('<slug:service_slug>/', ServiceDetailView.as_view(), name='service_details'),

]