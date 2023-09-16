from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='e-mail')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)

    verify_code = models.CharField(max_length=12, verbose_name='Код', **NULLABLE)
    is_verified = models.BooleanField(default=False, verbose_name='Верифицирован', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
