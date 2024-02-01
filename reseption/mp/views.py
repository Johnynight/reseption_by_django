from datetime import datetime

from django.shortcuts import render
from .forms import MyForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from docxtpl import DocxTemplate
import io

data = datetime.now().strftime("%d.%m.%Y")
time = datetime.today().time().strftime("%H:%M")


def main(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            number_mp = form.cleaned_data['number_mp']
            name_si = form.cleaned_data['name_si']
            osnovamie = form.cleaned_data['osnovamie']
            fio = form.cleaned_data['fio']
            vid_transfer = form.cleaned_data['vid_transfer']
            where = form.cleaned_data['where']
            owner = form.cleaned_data['owner']
            soglasoval = form.cleaned_data['soglasoval']

            document = DocxTemplate('reseption/mp/word_templates/template_docx.docx')
            context = {
                'number': number_mp,
                'name_si': name_si,
                'osnovaie': osnovamie,
                'name_osn': fio,
                'time': time,
                'car': vid_transfer,
                'where': where,
                'owner': owner,
                'why': soglasoval
            }
            # document.add_heading(f'Отчет от {name}', level=1)
            # document.add_paragraph(f'Имя: {name}')
            # document.add_paragraph(f'Email: {email}')
            # document.add_paragraph(f'Текст: {content}')
            document.render(context)

            # Создаем байтовый поток
            output = io.BytesIO()
            document.save(output)
            output.seek(0)

            # Отправляем файл в загрузку
            response = HttpResponse(
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename={name_si}.docx'
            response.write(output.read())
            print(number_mp)
            return response
    else:
        print('Error')
        form = MyForm()

    return render(request, 'mp/form.html', {'form': form})


def form2(request):
    form = MyForm()
    return render(request, 'mp/form.html', {'form': form})
