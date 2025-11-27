from django import forms

from .models import Reservation,User,MenuItems

class ReservationForm(forms.ModelForm):
    class Meta:
        model=Reservation
        fields='__all__'


class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['email','password']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['email','password','username','role']

class AddMenuForm(forms.ModelForm):
    class Meta:
        model=MenuItems
        fields='__all__'