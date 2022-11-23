from contact.models import Contact, ContactForm
from projects.models import ProjectDetail


def contact(request):
    return {'contact': Contact.objects.all()}

def contact_form(request):
    return {'contact_form': ContactForm.objects.all()}

def last_two_projects(request):
    return {'last_two_projects': ProjectDetail.objects.all().order_by('-id')[:2]}