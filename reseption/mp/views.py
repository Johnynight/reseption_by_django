from django.shortcuts import render
from .forms import MyForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from docxtpl import DocxTemplate
import io


def main(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            document = DocxTemplate('reseption/mp/word_templates/template_docx.docx')
            context = {
                'number' : name
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
            response['Content-Disposition'] = f'attachment; filename={name}.docx'
            response.write(output.read())

            return response
    else:
        form = MyForm()

    return render(request, 'mp/index.html', {'form': form})
