from django.shortcuts import render


# Create your views here.
def label(request):
    fake_content = {
        'titulo': 'titulo',
    }
    return render(request, 'label/label.html', context=fake_content)


def label_pdf_preview(request):
    context = {
        'etiquetas': [{'nome': 'Etiqueta 01',
                       'descricao': 'Descrição 01 Descrição 01 Descrição 01 Descrição 01 Descrição 01 Descrição 01',
                       'docura': 'Doçura 01'},
                      {'nome': 'Etiqueta 02', 'descricao': 'Descrição 02', 'docura': 'Doçura 02'},
                      {'nome': 'Etiqueta 03', 'descricao': 'Descrição 03', 'docura': 'Doçura 03'},
                      {'nome': 'Etiqueta 04', 'descricao': 'Descrição 04', 'docura': 'Doçura 04'},
                      {'nome': 'Etiqueta 05', 'descricao': 'Descrição 05', 'docura': 'Doçura 05'}]
    }
    return render(request, 'label/labelpreview.html', context=context)
