from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import inlineformset_factory
from .models import FolhaEtiqueta, FolhaEtiquetaItens
from .forms import FolhaEtiquetaForm, FolhaEtiquetaItensForm


# Create your views here.
@login_required
def label_pdf_preview(request, pk):
    folha_adesivos = get_object_or_404(FolhaEtiqueta, pk=pk)
    folha_adesivo_itens = folha_adesivos.folhaetiquetaitens_set.all()
    if folha_adesivos.modelo == 'BOLOS':
        folha_adesivo_template = 'label/labelpreviewbolos.html'
    else:
        folha_adesivo_template = 'label/labelpreviewlanches.html'

    context = {
        'folha': folha_adesivos.nome,
        'etiquetas': folha_adesivo_itens,
    }
    return render(request, template_name=folha_adesivo_template, context=context)


@login_required
def label_list(request):
    folhas = FolhaEtiqueta.objects.all()
    return render(request, 'label/list.html', {'folhas': folhas, })


@login_required
def label_create(request):
    folha_etiqueta_form = FolhaEtiqueta()
    folha_itens_formset = inlineformset_factory(
        FolhaEtiqueta, FolhaEtiquetaItens, form=FolhaEtiquetaItensForm, extra=0, can_delete=True,
        min_num=1, max_num=10, validate_min=True, validate_max=True
    )

    if request.method == 'POST':
        form = FolhaEtiquetaForm(request.POST, instance=folha_etiqueta_form, prefix='main')
        formset = folha_itens_formset(request.POST, instance=folha_etiqueta_form, prefix='product')

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect(label_list)

    else:
        form = FolhaEtiquetaForm(instance=folha_etiqueta_form, prefix='main')
        formset = folha_itens_formset(instance=folha_etiqueta_form, prefix='product')

    context = {
        'form': form,
        'formset': formset,
    }

    return render(request, 'label/create.html', context)


@login_required
def label_update(request, pk):
    folha_etiqueta = get_object_or_404(FolhaEtiqueta, pk=pk)
    folha_itens_formset = inlineformset_factory(
        FolhaEtiqueta, FolhaEtiquetaItens, form=FolhaEtiquetaItensForm, extra=0, can_delete=True,
        min_num=1, max_num=10, validate_min=True, validate_max=True
    )

    if request.method == 'POST':
        form = FolhaEtiquetaForm(request.POST, instance=folha_etiqueta, prefix='main')
        formset = folha_itens_formset(request.POST, instance=folha_etiqueta, prefix='product')

        try:
            if form.is_valid() and formset.is_valid():
                form.save()
                formset.save()
                messages.success(request, "A folha foi atualizada")
                return redirect(label_list)

        except Exception as e:
            messages.warning(request, 'Ocorreu um erro ao atualizar: {}'.format(e))

    else:
        form = FolhaEtiquetaForm(instance=folha_etiqueta, prefix='main')
        formset = folha_itens_formset(instance=folha_etiqueta, prefix='product')

    context = {
        'form': form,
        'formset': formset,
    }

    return render(request, 'label/update.html', context)
