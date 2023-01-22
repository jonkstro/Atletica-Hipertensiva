from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('plataforma/', views.plataforma, name='plataforma'),
    path('dados-associados/', views.dados_associados_listar, name="dados_associados_listar"),
    path('add-associado/', views.add_associado, name='add_associado'),
    path('carteirinha/<str:matricula>/', views.carteirinha, name='carteirinha'),
    path('buscar-carteirinha/', views.buscar_carteirinha, name='buscar_carteirinha'),



    # path('', views.plataforma, name='pg_inicial'),
    # path('dados_consumo/', views.dados_consumo, name='dados_consumo'),
    # path('dispositivos/', views.dispositivos, name='dispositivos'),
]