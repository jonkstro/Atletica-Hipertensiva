from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('plataforma/', views.plataforma, name='plataforma'),
    # path('', views.plataforma, name='pg_inicial'),
    # path('dados_consumo/', views.dados_consumo, name='dados_consumo'),
    # path('dispositivos/', views.dispositivos, name='dispositivos'),
]