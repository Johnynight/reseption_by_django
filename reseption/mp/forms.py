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
    number_mp = forms.IntegerField(label='Номер материального пропуска')
    name_si = forms.CharField(label='Наименование имущества', required=False)
    osnovamie = forms.CharField(label='Email', required=False)
    # fio = forms.CharField(label='Имя Фамилия', required=False)
    # # time_created = forms.DateTimeField(label='Время оформления пропуска')
    # vid_transfer = forms.CharField(label='Вид транспорта', required=False)
    # where = forms.CharField(label='Куда', required=False)
    # owner = forms.CharField(label='Пропуск выдал:', required=False)
    # soglasoval = forms.CharField(label='Согласовал ->', required=False)