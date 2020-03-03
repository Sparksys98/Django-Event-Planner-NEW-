from django import forms
from django.contrib.auth.models import User

from .models import Event, Booking
class UserSignup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }


class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class CreateForm(forms.ModelForm):
    class Meta:
        model=Event
        exclude=['added_by']

class DetailForm(forms.ModelForm):
    class Meta:
        model=Event
        fields=[ 'title', 'description', 'datetime','location','seats','added_by']

class BookForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields = ['tickets']
