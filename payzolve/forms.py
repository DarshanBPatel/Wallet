

from django import forms
from .models import wallet


class formsignup(forms.ModelForm):

    class Meta:
        model = wallet
        fields = ('first_name', 'last_name', "mobile_number", 'password')


class formlogin(forms.ModelForm):

    class Meta:
        model = wallet
        fields = ('mobile_number', 'password')


class formCredit(forms.Form):
    balance = forms.IntegerField()
    # t = "c"


class formDebit(forms.Form):
    balance = forms.IntegerField()
    # t = "d"
