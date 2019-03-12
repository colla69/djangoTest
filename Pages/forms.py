from django import forms

from .models import Store

class StoreForm(forms.ModelForm):
    title = forms.CharField()
    desc = forms.CharField(required=False,
                           widget=forms.Textarea())
    price = forms.CharField()

    email = forms.EmailField()
    class Meta:
        model = Store
        fields =[
            'title',
            'desc',
            'price'
        ]

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")#
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a Valid Email")

class RawStoreForm(forms.Form):
    title = forms.CharField()
    desc = forms.CharField(required=False,
                            widget=forms.Textarea())
    price = forms.CharField()