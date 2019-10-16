from django.urls import path

from . import views

urlpatterns = [
    path('', views.label, name='label'),
    path('pdf/', views.label_pdf_preview, name='pdf_preview'),
]
