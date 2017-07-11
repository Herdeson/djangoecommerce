from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from .models import User
from .forms import UserAdminCreatForm

from django.contrib.auth.mixins import LoginRequiredMixin

# Usado quando for uma view baseada em função
# from django.contrib.auth.decorators import login_required

# Create your views here.

class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreatForm
    success_url = reverse_lazy('index')

register = RegisterView.as_view()

# A ordem é importante LoginRequiredMixin
class IndexView( LoginRequiredMixin , TemplateView):
    template_name = 'accounts/index.html'

index = IndexView.as_view()

class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user

update_user = UpdateUserView.as_view()

class UpdatePasswordView(LoginRequiredMixin, FormView ):
    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)

update_password = UpdatePasswordView.as_view()
