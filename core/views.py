from django.shortcuts import render
from django.http import HttpResponse
#from django.core.mail import send_mail
from catalog.models import Category

from django.conf import settings
# from djangoecommerce import settings # Nunca fazer dessa forma
from .forms import ContactForm

# Create your views here.

def index(request):
    #return HttpResponse('Helo World!')
    #context = {
    #    'categories': Category.objects.all()
    #}

    return render( request ,'index.html' )
"""
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

    context = {
        'form': form,
        'success': success
    }
    return render(request,'contact.html', context)


#def product_list(request):
#    return render(request, 'product_list.html')



def product(request):
    return render(request, 'product.html')
