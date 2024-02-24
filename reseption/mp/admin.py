from django.contrib import admin
from .models import Material_pass
from django.http import HttpResponse
import csv


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

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

        fieldnames = [  # здесь вы можете указать имена полей вашей модели Material_pass
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
        ]

        writer = csv.DictWriter(response, fieldnames=fieldnames)
        writer.writeheader()

        for obj in queryset:
            writer.writerow({field: getattr(obj, field) for field in fieldnames})

        return response

    export_to_csv.short_description = "Экспортировать в CSV"  Определяем отображаемое имя для действия

    actions = ['export_to_csv']


admin.site.register(Material_pass, Mp_admin)
