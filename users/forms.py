from django.contrib.auth.forms import UserCreationForm
from users.models import User
from products.forms import StyleFormMixin


class UserForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
