from django.shortcuts import render, redirect
from datetime import datetime
from django.views.generic import View, ListView
from .models import Contact, PhoneNumberField, ContactForm
from .forms import UserForm
from django.core.mail import BadHeaderError
from django.views.generic.edit import FormView
from django.core.mail import send_mail


# class ContactView(ListView):
#     model = Contact
#     template_name = 'contact.html'
#     context_object_name = 'contact' # вынесено в ContextProcessors


class ContactFormView(FormView):
    model = ContactForm
    form_class = UserForm
    template_name = 'contacts.html'
    success_url = 'thanks'

    def form_valid(self, myform):
        myform.send_mail()
        myform.save()  # сохранение в БД
        return super().form_valid(myform)

    def form_invalid(self, myform):
        return redirect('/uploads_error')



# def feedback(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save()
#             return redirect('thanks')
#     else:
#         form = UserForm()
#     return render(request, 'contacts.html', {'form': form,})
