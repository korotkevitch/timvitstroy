from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView
from .models import ServicePage, ServiceDetail

class ServicePageView(ListView):
    model = ServicePage
    template_name = 'services.html'
    context_object_name = 'page_services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['service_page_services'] = ServiceDetail.objects.all()
        return context


class ServiceDetailView(ListView):
    template_name = 'service_details.html'
    context_object_name = 'current_service_details'

    def get_queryset(self):
        return get_object_or_404(ServiceDetail, slug=self.kwargs['service_slug'])

