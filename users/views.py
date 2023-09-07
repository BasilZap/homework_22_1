from django.shortcuts import render
from users.forms import UserForm
from django.urls import reverse_lazy
from users.models import User
from django.views.generic import CreateView


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('products:list')
    template_name = 'users/register.html'
