# employee/urls.py

from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('emp', views.emp, name='emp'),
    path('show', views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.destroy, name='delete'),
]
