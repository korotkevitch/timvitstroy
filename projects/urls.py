from django.urls import path
from projects import views
from .views import ProjectPageView, ProjectDetailView, IndProjectPageView


urlpatterns = [
    path('', IndProjectPageView.as_view(), name='projects'),
    path('<slug:section_slug>/<slug:project_slug>/', ProjectDetailView.as_view(), name='project_details'),
]