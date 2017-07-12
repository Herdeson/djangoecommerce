from django.shortcuts import render
from django.http import HttpResponse
#from django.core.mail import send_mail
from catalog.models import Category

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View, TemplateView, CreateView
# from djangoecommerce import settings # Nunca fazer dessa forma
from .forms import ContactForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
# Create your views here.

class IndexView(TemplateView):

    template_name = 'index.html'

    #def get(self, request):
    #    return render(request, 'index.html')

index = IndexView.as_view()


"""
def index(request):
    #return HttpResponse('Helo World!')
    #context = {
    #    'categories': Category.objects.all()
    #}
    return render( request ,'index.html' )


def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            email = 'Nome: {0}\nE-mail:{1}\n{2}'.format(dados['name'], dados['email'], dados['message'])
            send_mail('Contato - Campo Assunto', email, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL] )
            success = True
    else:
        form = ContactForm()
    context = {
        'form': form,
        'success': success
    }
    return render(request,'contact.html', context)
"""



def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render(request,'contact.html', context)


#def product_list(request):
#    return render(request, 'product_list.html')

#User = get_user_model()

def product(request):
    return render(request, 'product.html')
"""
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    model = User
    success_url = reverse_lazy('index')

register = RegisterView.as_view()
"""
