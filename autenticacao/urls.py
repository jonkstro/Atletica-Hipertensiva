from unicodedata import name
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    # path('cadastro/', views.cadastro, name='cadastro'),
    # path('ativar_conta/<str:token>/', views.ativar_conta, name="ativar_conta"),
    path('', views.logar, name='logar'),
    path('sair/', views.sair, name="sair"),
    path('forgot/', views.forgot, name='forgot'),
    path('alterar_senha/<str:token>/', views.alterar_senha, name='alterar_senha'),
]