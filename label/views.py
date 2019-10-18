from django.shortcuts import render, get_object_or_404
from .models import FolhaEtiqueta


# Create your views here.
def label_pdf_preview(request, pk):
    folha_adesivos = get_object_or_404(FolhaEtiqueta, pk=pk)
    folha_adesivo_itens = folha_adesivos.folhaetiquetaitens_set.all()
    context = {
        'etiquetas': folha_adesivo_itens,
    }
    return render(request, 'label/labelpreview.html', context=context)
