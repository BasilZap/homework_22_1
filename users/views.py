from django.shortcuts import redirect, render

from users.forms import UserRegisterForm, UserForm
from django.urls import reverse_lazy, reverse
from users.models import User
from django.views.generic import CreateView, UpdateView


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('products:list')
    template_name = 'users/register.html'


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user

