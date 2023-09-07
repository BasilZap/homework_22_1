from users.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='vnzapr@yandex.ru',
            first_name='admin',
            last_name='Basil',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123456')
        user.save()

