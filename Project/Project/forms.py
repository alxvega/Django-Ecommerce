from django import forms
# from django.contrib.auth.models import User. I'm replacing Django's default User model to use my own
from users.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=4, max_length=16, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                                         'id': 'username',
                                                                                                         'placeholder': 'Username'
                                                                                                         }))
    email = forms.EmailField(required=True, min_length=8, max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'placeholder': 'Email'
    }))
    password = forms.CharField(required=True, min_length=6, max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                                             'id': 'password',
                                                                                                             'placeholder':     'Password'
                                                                                                             }))
    password2 = forms.CharField(label='Confirm password', required=True, min_length=6, max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                                                                        'id': 'password',
                                                                                                                                        'placeholder':     'Contraseña'
                                                                                                                                        }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Username is already registered.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Email is already registered.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'Passwords do not match')

    def save(self):
        return User.objects.create_user(self.cleaned_data.get('username'),
                                        self.cleaned_data.get('email'),
                                        self.cleaned_data.get('password'))
