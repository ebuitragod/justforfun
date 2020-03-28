from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    identification = forms.CharField(max_length=10, help_text='Required') #Espe
    email = forms.CharField(max_length=254, help_text='Required. Please inform a valid email address.')
    phone = forms.CharField(max_length=10, required=False, help_text='Optional') #Espe
    user_type = forms.CharField(max_length=10, help_text='Write one option pacient, physician, or hospital')

    class Meta:
        model = User
        fields = ('username', 'identification', 'first_name', 'last_name', 'email', 'phone', 'user_type', 'password1', 'password2', )

