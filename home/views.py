from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Head, About, Service, Testimonial
from projects.models import ProjectDetail, ProjectSection

class HomeView(ListView):
    model = Head
    template_name = 'index.html'
    context_object_name = 'head'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['about'] = About.objects.all()
        context['services'] = Service.objects.all()
        context['all_projects'] = ProjectDetail.objects.all()
        context['all_sections'] = ProjectSection.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        return context
