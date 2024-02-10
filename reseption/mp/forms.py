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
    item = forms.CharField(label='Наименование имущества', required=False)
    osnovamie = forms.CharField(label='Основание', required=False)
    osnovamie_dop = forms.CharField(label='Само основание', required=False)
    first_name = forms.CharField(label='Имя', required=False)
    last_name = forms.CharField(label='Фамилия', required=False)
    # time_created = forms.DateTimeField(label='Время оформления пропуска')
    car = forms.CharField(label='Вид транспорта', required=False)
    car_dop = forms.CharField(label='Доп. вид трансфера', required=False)
    name_driver = forms.CharField(label='ФИО водителя', required=False)
    name_driver_dop = forms.CharField(label='ФИО водителя', required=False)
    # rrr = forms.CharField(label='machine', required=False)
    # rrr_2 = forms.CharField(label='machine_2', required=False)
    where = forms.CharField(label='Куда', required=False)
    where_dop = forms.CharField(label='Куда', required=False)
    owner = forms.CharField(label='Пропуск выдал:', required=False)
    soglasoval = forms.CharField(label='Согласовал ->', required=False)
