from django import forms
from .models import Manager

class ManagerSignupForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['first_name', 'last_name', 'email', 'company_name','password']
