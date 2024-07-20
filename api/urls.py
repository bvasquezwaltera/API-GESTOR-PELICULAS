from django.urls import path
from .views import EmpresaView

urlpatterns = [
    path('empresas/',EmpresaView.as_view(),name='empresas'),
]
