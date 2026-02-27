from django.urls import path
from . import views

urlpatterns = [
    path('abune/', views.abune_ol, name='abune-ol'),
    path('elaqe/', views.elaqe_gonder, name='elaqe-gonder'),
]
