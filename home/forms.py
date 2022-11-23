from django import forms
from django.forms import ModelForm, Textarea
from home.models import About, Service, Testimonial
from services.models import ServicePage
from gallery.models import GalleryPage
from projects.models import ProjectPage, ProjectDetail, IndProjectPage



class AboutForm(ModelForm):

    class Meta:
        model = About
        fields = '__all__'
        widgets = {
            'text': Textarea(attrs={'cols': 160,
                                    'rows': 20})
        }


class ServiceForm(ModelForm):

    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'text': Textarea(attrs={'cols': 160,
                                    'rows': 20})
        }


class ServicePageForm(ModelForm):

    class Meta:
        model = ServicePage
        fields = '__all__'
        widgets = {
            'text': Textarea(attrs={'cols': 160,
                                    'rows': 20}),
            'bottom_text': Textarea(attrs={'cols': 160,
                                    'rows': 20})
        }


class GalleryPageForm(ModelForm):

    class Meta:
        model = GalleryPage
        fields = '__all__'
        widgets = {
            'bottom_text': Textarea(attrs={'cols': 160,
                                    'rows': 20}),
        }


class IndProjectPageForm(ModelForm):

    class Meta:
        model = IndProjectPage
        fields = '__all__'
        widgets = {
            'text': Textarea(attrs={'cols': 160,
                                    'rows': 20}),
        }


class TestimonialForm(ModelForm):

    class Meta:
        model = Testimonial
        fields = '__all__'
        widgets = {
            'testimonial': Textarea(attrs={'cols': 160,
                                    'rows': 20}),
        }


# class ProjectPageForm(ModelForm):
#
#     class Meta:
#         model = ProjectPage
#         fields = '__all__'
#         widgets = {
#             'bottom_text': Textarea(attrs={'cols': 160,
#                                     'rows': 20}),
#         }


# class ProjectDetailForm(ModelForm):
#
#     class Meta:
#         model = ProjectDetail
#         fields = '__all__'
#         widgets = {
#             'article_text': Textarea(attrs={'cols': 160,
#                                     'rows': 20}),
#         }