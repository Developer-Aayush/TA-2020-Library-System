from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.forms import fields
from django.forms import widgets

from library.models import allInformation

from .models import allInformation

from django.forms import ModelForm

User = get_user_model()


class UserLoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

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


class allInformationForm(forms.ModelForm):
    class Meta:
        model = allInformation
        fields = ('Book_name', 'Authors_Name',
                  'Book_Type', 'Book_serial_Number', 'Book_Price', 'Publication_Name', 'Book_Quantity')

        widgets = {
            'Book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Authors_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Book_Type': forms.TextInput(attrs={'class': 'form-control'}),
            'Book_serial_Number': forms.TextInput(attrs={'class': 'form-control'}),
            'Book_Price': forms.TextInput(attrs={'class': 'form-control'}),
            'Publication_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Book_Quantity': forms.TextInput(attrs={'class': 'form-control'}),

        }
