from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        send_mail(
            f"Contact form submission from {self.cleaned_data['name']}",
            self.cleaned_data['message'],
            self.cleaned_data['email'],
            ['admin@electronicsstore.com'],
        )