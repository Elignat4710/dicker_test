from django import forms
from .models import MySimpleModel


class Form(forms.ModelForm):

    class Meta:
        model = MySimpleModel
        fields = ['text']
