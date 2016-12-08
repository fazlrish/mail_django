# coding=utf-8
from django import forms
from django.forms import ModelForm

from review.models import User

#Registration form based on User model
class UserRegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label=u'Пароль')
    class Meta:
        model = User
        fields = ('email','username','password')


#Authorization form based on User model
class UserAuthorizationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label=u'Пароль')
    class Meta:
        model = User
        fields = ('username','password')

