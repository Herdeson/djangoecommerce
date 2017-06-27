from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget = forms.Textarea)
"""
    Pode ser construido os formularios dessa forma, porem o codigo python fica responsavel por pela construçao do layout
    e fica invasivo. O ideal é alterar diretamente no template. Em opção a isso poderiamos usar o django-widget-tweaks

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['class'] = 'form-control'
"""
