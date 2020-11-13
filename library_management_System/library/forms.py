from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.forms import fields
from django.forms import widgets

from library.models import allInformation

from .models import allInformation

from django.forms import ModelForm

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


# class addBooks(forms.Form):
#     Serial_Number = forms.CharField()
#     Book_Name = forms.CharField()
#     Book_Type = forms.CharField()
#     Author_Name = forms.CharField()
#     Book_Price = forms.IntegerField()

class allInformationForm(ModelForm):
    class Meta:
        model = allInformation
        fields = '__all__'
