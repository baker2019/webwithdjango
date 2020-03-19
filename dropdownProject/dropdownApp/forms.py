from django.forms import ModelForm,modelformset_factory,formset_factory
from django import forms
from .models import Country

class CountryForm(ModelForm):
    name = forms.CharField(widget=forms.Select)
    class Meta:
        model = Country
        fields = ('name',)