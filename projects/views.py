from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView
from .models import ProjectPage, ProjectDetail, ProjectSection, IndProjectPage


class IndProjectPageView(ListView):
    model = IndProjectPage
    template_name = 'ind_projects.html'
    context_object_name = 'page_ind_projects'


class ProjectPageView(ListView):
    model = ProjectPage
    template_name = 'projects.html'
    context_object_name = 'page_projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['all_projects'] = ProjectDetail.objects.all()
        context['all_sections'] = ProjectSection.objects.all()
        return context


class ProjectDetailView(ListView):
    template_name = 'project_details.html'
    context_object_name = 'current_project_details'

    def get_queryset(self):
        return get_object_or_404(ProjectDetail, slug=self.kwargs['project_slug'])

    def get_context_data(self, **kwargs):
        self.section = get_object_or_404(ProjectSection, slug=self.kwargs['section_slug'])
        context = super().get_context_data()
        context['page_projects'] = ProjectPage.objects.all()
        context['section_projects'] = ProjectDetail.objects.filter(section=self.section)
        context['last_projects'] = ProjectDetail.objects.all().exclude(slug=self.kwargs['section_slug']).exclude(slug=self.kwargs['project_slug']).order_by('-id')[:3]
        return context
