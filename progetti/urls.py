from django.urls import path
from django.views.generic import RedirectView

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('progetti/', views.ProgettoList.as_view(), name='progetti'),
    path('progetti/<int:pk>/', views.ProgettoDetail.as_view(), name='progetti-detail'),

    path('docenti/', views.UserList.as_view(), name='docenti'),
    path('docenti/<int:pk>/', views.UserDetail.as_view(), name='docenti-detail'),

    path('materiali/', views.MaterialeList.as_view(), name='materiali'),
    path('materiali/<int:pk>/', views.MaterialeDetail.as_view(), name='materiali-detail'),

    path('esterni/', views.EsternoList.as_view(), name='esterni'),
    path('esterni/<int:pk>/', views.EsternoDetail.as_view(), name='esterni-detail'),

    path('fs/', views.FunzioneStrumentaleList.as_view(), name='fs'),
    path('fs/<int:pk>/', views.FunzioneStrumentaleDetail.as_view(), name='fs-detail'),

    path('', RedirectView.as_view(url='progetti/', permanent=True)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
