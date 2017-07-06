from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView
from django.core.urlresolvers import reverse_lazy
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

# A ordem é importante
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
