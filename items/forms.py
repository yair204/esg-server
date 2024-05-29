from django import forms
from .models import Item , Category

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'category']

    category = forms.ModelChoiceField(queryset=Category.objects.all())
