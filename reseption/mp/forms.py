from django import forms
from .models import Material_pass


class Form_mp(forms.ModelForm):
    class Meta:
        model = Material_pass
        fields = [
            'serial_number',
            'name_property'
        ]


class MyForm(forms.Form):
    name = forms.CharField(label='Имя')
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Текст', widget=forms.Textarea)