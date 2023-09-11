from django.shortcuts import redirect, render
from django.core.mail import send_mail
from users.forms import UserRegisterForm, UserForm
from django.urls import reverse_lazy, reverse
from users.models import User
from django.views.generic import CreateView, UpdateView
from config.settings import EMAIL_HOST_USER
from random import randint


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('products:login')
    template_name = 'users/register.html'


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user

    # def form_valid(self, form):
    #
    #     if form.is_valid():
    #         self.object = form.save()
    #         if form.data.get('pass_gen', False):
    #             new_pass = self.object.make_random_password(length=12)
    #             send_mail(
    #                         subject='Смена пароля',
    #                         message=f'Ваш новый пароль {new_pass}',
    #                         from_email=EMAIL_HOST_USER,
    #                         recipient_list=[self.request.user.email]
    #                     )
    #             self.object.set_password()
    #             self.object.save()
    #
    #     return super().form_valid(form)


def generate_password(request):
    new_pass = ''.join(str(randint(0, 9)) for _ in range(9))
    send_mail(
        subject='Смена пароля',
        message=f'Ваш новый пароль {new_pass}',
        from_email=EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_pass)
    request.user.save()
    return redirect(reverse('products:login'))
