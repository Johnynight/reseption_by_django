from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Material_pass


class Mp_admin(admin.ModelAdmin):
    list_display = (
        'serial_number',
        'name_property',
        'reason',
        'owner_reason',
        'time_registration',
        'type_transport',
        'where',
        'issued_pass',
        'today_data',
        'approved'
    )

    list_editable = (
        'reason',
        'owner_reason',
        'time_registration',
        'type_transport',
        'where',
        'issued_pass',
        'today_data',
        'approved'
    )

    list_display_links = ('name_property',)  # Установка поля name_property в качестве ссылки на редактирование

admin.site.register(Material_pass, Mp_admin)

