from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contrate/', views.contrato, name='meContrate'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('excluir_mensagem/<int:contato_id>/', views.excluir_mensagem, name='excluir_mensagem'),
    path('marcar_como_lido/<int:contato_id>/', views.marcar_como_lido, name='marcar_como_lido'),
    path('marcar_como_nao_lido/<int:contato_id>/', views.marcar_como_nao_lido, name='marcar_como_nao_lido'),
]