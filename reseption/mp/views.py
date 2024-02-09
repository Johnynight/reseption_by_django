import pprint
from datetime import datetime
from .models import Material_pass
from django.shortcuts import render
from .forms import MyForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from docxtpl import DocxTemplate
import io
from django.utils import timezone

data = datetime.now().strftime("%d.%m.%Y")
time = datetime.today().time().strftime("%H:%M")


def main(request):
    number_mp = Material_pass.objects.last()
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            number_mp = form.cleaned_data['number_mp']
            name_si = form.cleaned_data['name_si']
            osnovamie = form.cleaned_data['osnovamie'] + form.cleaned_data['osnovamie_dop']
            fio = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']
            vid_transfer = form.cleaned_data['vid_transfer']
            car = form.cleaned_data['rrr']
            where = form.cleaned_data['www']
            owner = form.cleaned_data['owner']
            soglasoval = form.cleaned_data['soglasoval']
            # / home / teqilkka / media / template_docx.docx
            document = DocxTemplate(
                'reseption/mp/word_templates/template_docx.docx')  # /home/teqilkka/media/template_docx.docx
            if osnovamie == 'custom':
                osnovamie = form.cleaned_data['osnovamie_dop']
            if vid_transfer == 'custom':
                vid_transfer = form.cleaned_data['vid_transfer_dop']
            if where == 'custom':
                where = form.cleaned_data['where_dop ']
            if car == 'custom':
                car = form.cleaned_data['rrr_2']

            context = {
                'number': number_mp,
                'name_si': name_si,
                'osnovaie': osnovamie,
                'name_osn': fio,
                'time': time,
                'car': car,
                'gos_number': vid_transfer,
                'where': where,
                'owner': owner,
                'why': soglasoval
            }

            document.render(context)

            # Создаем байтовый поток
            output = io.BytesIO()
            document.save(output)
            output.seek(0)

            # Отправляем файл в загрузку
            response = HttpResponse(
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename="Material_pass_{number_mp}".docx'
            response.write(output.read())
            pprint.pprint(context)
            new_entry = Material_pass(
                serial_number=number_mp,
                name_property=name_si,
                owner_reason=fio,
                reason=osnovamie,
                time_registration=timezone.now(),
                type_transport=vid_transfer,
                where=where,
                issued_pass=owner,
                today_data=timezone.now(),
                approved=soglasoval
            )

            new_entry.save()

            return response
    else:
        print('Error')

        form = MyForm()

    return render(request, 'mp/sample.html', {'form': form,
                                              'number_mp': number_mp.serial_number + 1})


def form2(request):
    form = MyForm()
    return render(request, 'mp/form.html', {'form': form})
