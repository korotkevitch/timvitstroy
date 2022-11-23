from django.contrib import admin


from projects.models import IndProjectPage
from home.forms import IndProjectPageForm
class IndProjectPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'text_title', 'text', 'banner_preview', 'image_preview')
    form = IndProjectPageForm
    list_display_links = ('id', 'title')
admin.site.register(IndProjectPage, IndProjectPageAdmin)


# from projects.models import ProjectSection
# class ProjectSectionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'section', 'alias', 'slug')
#     list_display_links = ('id', 'section')
#     prepopulated_fields = {'alias': ('section',),
#                            'slug': ('section',)
#                            }
# admin.site.register(ProjectSection, ProjectSectionAdmin)


# from projects.models import ProjectPage
# from home.forms import ProjectPageForm
# class ProjectPageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'subtitle', 'bottom_title', 'bottom_text', 'banner_preview')
#     form = ProjectPageForm
#     list_display_links = ('id', 'title')
# admin.site.register(ProjectPage, ProjectPageAdmin)


# from projects.models import ProjectDetail
# from home.forms import ProjectDetailForm
# class ProjectDetailAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'section', 'description', 'image_preview', 'slug', 'article_photo_preview',
#                     'article_thumb_preview', 'article_name', 'article_trim')
#     list_display_links = ('id', 'name')
#     form = ProjectDetailForm
#     prepopulated_fields = {'slug': ('name',)}
# admin.site.register(ProjectDetail, ProjectDetailAdmin)
