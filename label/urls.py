from django.urls import path

from . import views

urlpatterns = [
    path('pdf/<int:pk>', views.label_pdf_preview, name='pdf_preview'),
]
