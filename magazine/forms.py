from django import forms
from article.models import User

class Registration(forms.Form):
    model=User
    # fields=['first_name','last_name','user_name','e_mail','password']
    first_name=forms.CharField()
    last_name=forms.CharField()
    user_name=forms.CharField()
    e_mail= forms.EmailField()
    password =forms.CharField(widget=forms.PasswordInput)
    Confirm_password =forms.CharField(widget=forms.PasswordInput)

   