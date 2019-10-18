from django.contrib import admin

from .models import FolhaEtiqueta, FolhaEtiquetaItens


# Register your models here.
class FolhaEtiquetaItensInline(admin.StackedInline):
    model = FolhaEtiquetaItens
    extra = 0
    max_num = 8


class FolhaEtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [
        FolhaEtiquetaItensInline,
    ]


admin.site.register(FolhaEtiqueta, FolhaEtiquetaAdmin)
