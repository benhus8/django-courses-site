from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'birthday', 'phone_number',
                  'address', 'building_number', 'postal_code', 'city']


class EditUserDataForm(UserChangeForm):
    # excluding username and password from form
    password1 = None
    password2 = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'birthday', 'phone_number',
                  'address', 'building_number', 'postal_code', 'city']
