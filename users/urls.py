from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView, UserUpdateView, generate_password, verify_email, get_verify
from users.apps import UsersConfig


app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/pass_gen', generate_password, name='generate_password'),
    path('profile/email_verify', get_verify, name='get_verify'),
    path('register/verify', verify_email, name='verify_email'),
]
