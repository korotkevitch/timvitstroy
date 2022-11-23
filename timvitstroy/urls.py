"""timvitstroy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from contact.views import ContactFormView

admin.site.site_header = 'ТимВитСтрой'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('services/', include('services.urls')),
    path('gallery/', include('gallery.urls')),
    path('projects/', include('projects.urls')),
    path('base/', TemplateView.as_view(template_name='base.html')),
    path('navbar/', TemplateView.as_view(template_name='includes/navbar.html')),
    path('footer/', TemplateView.as_view(template_name='includes/footer.html')),
    path('contacts/', include('contact.urls')),
    path('contact_form', ContactFormView.as_view(), name="contact_form"),
    path('thanks/', TemplateView.as_view(template_name='thanks.html')),
    path('uploads_error/', TemplateView.as_view(template_name='uploads_error.html')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
