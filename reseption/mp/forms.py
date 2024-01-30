from django import forms
from .models import Material_pass


class Form_mp(forms.ModelForm):
    class Meta:
        model = Material_pass
        fields = [
            'serial_number',
            'name_property'
        ]
