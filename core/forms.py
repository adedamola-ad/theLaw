from django import forms
from .models import Contact


class ContactForm(forms.Form):
	name = forms.CharField()
	phone_number = forms.IntegerField()
	email = forms.CharField()
	message = forms.CharField()


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'email', 'message']