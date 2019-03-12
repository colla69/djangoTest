from django import forms

from .models import Store

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields =[
            'title',
            'desc',
            'price'
        ]

class RawStoreForm(forms.Form):
    title = forms.CharField()
    desc = forms.CharField()
    price = forms.CharField()