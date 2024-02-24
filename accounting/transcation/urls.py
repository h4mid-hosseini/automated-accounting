from . import views
from django.urls import path


app_name = 'transcations'

urlpatterns = [
    path('auto/', views.auto_register, name='auto')
]