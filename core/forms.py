from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget = forms.Textarea)

    def send_mail(self):
        dados = self.cleaned_data
        email = 'Nome: {0}\nE-mail:{1}\n{2}'.format(dados['name'], dados['email'], dados['message'])
        send_mail('Contato - Campo Assunto', email, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL] )

"""
    Pode ser construido os formularios dessa forma, porem o codigo python fica responsavel por pela construçao do layout
    e fica invasivo. O ideal é alterar diretamente no template. Em opção a isso poderiamos usar o django-widget-tweaks

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['class'] = 'form-control'
"""
