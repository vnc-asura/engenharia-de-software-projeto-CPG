from django.urls import path
from . import views

urlpatterns = [
    path('patrimonios/', views.listar_patrimonios, name='listar_patrimonios'),
    path('patrimonios/novo/', views.criar_patrimonio, name='criar_patrimonio'),
    path('patrimonios/<int:id>/editar/', views.editar_patrimonio, name='editar_patrimonio'),
    path('patrimonios/<int:pk>/excluir/', views.excluir_patrimonio, name='excluir_patrimonio'),
    # path('inventarios/', views.listar_inventarios, name='listar_inventarios'),
    # path('emprestimos/', views.listar_emprestimos, name='listar_emprestimos'),
]