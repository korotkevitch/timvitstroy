from django.contrib import admin

from contact.models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'phone_link', 'viber', 'viber_link', 'address', 'email', 'banner_preview')
    list_display_links = ('id', 'phone')
admin.site.register(Contact, ContactAdmin)


from .models import ContactForm
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'message', 'file')
    list_display_links = ('id', 'name')
admin.site.register(ContactForm, ContactFormAdmin)
