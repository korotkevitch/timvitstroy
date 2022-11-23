from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView
from projects.models import ProjectDetail


class LastProjectView(ListView):
    template_name = 'footer.html'
    context_object_name = 'last_projects'

    def get_queryset(self):
        return ProjectDetail.objects.all().order_by('-id')[:2]
