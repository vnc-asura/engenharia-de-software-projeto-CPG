from django.urls import path
from . import views

urlpatterns = [
    path('patrimonios/', views.listar_patrimonios, name='listar_patrimonios'),
    path('inventarios/', views.listar_inventarios, name='listar_inventarios'),
    path('emprestimos/', views.listar_emprestimos, name='listar_emprestimos'),
]