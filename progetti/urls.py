from django.urls import path
from django.views.generic import RedirectView

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('progetti/', views.ProgettoList.as_view()),
    path('progetti/<int:pk>/', views.ProgettoDetail.as_view()),

    path('docenti/', views.DocenteList.as_view()),
    path('docenti/<int:pk>/', views.DocenteDetail.as_view()),

    path('materiali/', views.MaterialeList.as_view()),
    path('materiali/<int:pk>/', views.MaterialeDetail.as_view()),

    path('esterni/', views.EsternoList.as_view()),
    path('esterni/<int:pk>/', views.EsternoDetail.as_view()),

    path('fs/', views.FunzioneStrumentaleList.as_view()),
    path('fs/<int:pk>/', views.FunzioneStrumentaleDetail.as_view()),

    path('', RedirectView.as_view(url='progetti/', permanent=True)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
