from django.shortcuts import redirect, render
from django.core.mail import send_mail
from users.forms import UserRegisterForm, UserForm
from django.urls import reverse_lazy, reverse
from users.models import User
from django.views.generic import CreateView, UpdateView
from config.settings import EMAIL_HOST_USER
from random import randint
from django.contrib import messages


# Контроллер регистрации пользователя
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('products:list')
    template_name = 'users/register.html'


# Контроллер редактирования пользователя
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
    """
    Контроллер генерации пароля пользователя и отправки его по email
    """
    new_pass = ''.join(str(randint(0, 9)) for _ in range(8))
    send_mail(
        subject='Смена пароля',
        message=f'Ваш новый пароль {new_pass}',
        from_email=EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    # Запоминаем и сохраняем пароль
    request.user.set_password(new_pass)
    request.user.save()
    return redirect(reverse('users:login'))


def verify_email(request):
    """
    Контроллер верификации пользователя перешедшего по ссылке
    из email
    """
    # Получаем из get-запроса с формы pk и код
    user_pk = request.GET.get('pk')
    code = request.GET.get('code')
    # Проверка что pk число для предотвращения ошибки
    if user_pk.isdigit():
        # Проверка того, что код и pk пользователя совпадают с данными текущего пользователя
        if request.user.verify_code == code and request.user.pk == int(user_pk):
            request.user.is_verified = True
            request.user.save()     # Если данные совпали - устанавливаем флаг is_verified и сохраняем
            messages.success(request, 'Верификация пройдена ')
            return redirect(reverse('users:profile'))
        else:
            # Если код и pk пользователя не совпадают с данными текущего пользователя - выдаем ошибку
            messages.error(request, f"Верификация не пройдена, перейдите по ссылке из email ")
    else:
        # pk не число - выдаем ошибку
        messages.error(request, f"Некорректные данные")

    return render(request, 'users/verify_email.html')


def password_recover(request):
    """
    Контроллер верификации пользователя перешедшего по ссылке
    из email
    """
    # Если метод POST проверяем наличие пользователя с указанным email в базе
    if request.method == 'POST':
        user_email = request.POST.get('email')
        print(user_email)

        # Если пользователь найден - генерируем новый пароль, сохраняем и отправляем по почте
        if User.objects.get(email=user_email):
            user = User.objects.get(email=user_email)
            print(user.pk)

            new_pass = ''.join(str(randint(0, 9)) for _ in range(8))
            send_mail(
                subject='Смена пароля',
                message=f'Ваш новый пароль {new_pass}',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
            # Запоминаем и сохраняем пароль
            user.set_password(new_pass)
            user.save()
            # Перенаправляем на страницу входа
            return redirect(reverse('users:login'))
    return render(request, 'users/password_recover.html')


def get_verify(request):
    """
    Контроллер запроса на верификацию. Генерирует проверочный код
    для пользователя, формирует ссылку для проверки.
    """
    # Получаем данные пользователя
    user_pk = request.user.pk
    user_mail = request.user.email
    v_code = ''.join(str(randint(0, 9)) for _ in range(6))  # Генерируем проверочный код
    request.user.verify_code = v_code
    request.user.save()     # Запоминаем проверочный код и сохраняем в базе
    send_mail(
        subject='Пройдите верификацию, перейдите по ссылке:',
        message=f'http://127.0.0.1:8000/users/register/verify?pk={user_pk}&code={v_code}',
        from_email=EMAIL_HOST_USER,
        recipient_list=[user_mail]
    )       # Отправляем email с проверочной ссылкой пользователю
    print(f'http://127.0.0.1:8000/users/register/verify?pk={user_pk}&code={v_code}')  # Дублируем ссылку в консоль
    return redirect(reverse('users:profile'))
