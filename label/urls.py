from django.urls import path

from . import views

urlpatterns = [
    path('', views.label_list, name='label_list'),
    path('pdf/<int:pk>', views.label_pdf_preview, name='pdf_preview'),
    path('create/', views.label_create, name='label_create'),
    path('update/<int:pk>', views.label_update, name='label_update'),
]
