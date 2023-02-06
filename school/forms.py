from django.forms import ModelForm
from django import forms
from .models import StudentRegisteration


class StudentForm(ModelForm):
    class Meta:
        model = StudentRegisteration
        widgets = {
        'password': forms.PasswordInput(),}
        fields = '__all__'

class LoginPage(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())