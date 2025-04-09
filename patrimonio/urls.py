from django.urls import path
from . import views

urlpatterns = [
    path('patrimonios/', views.listar_patrimonios, name='listar_patrimonios'),
    path('patrimonios/novo/', views.criar_patrimonio, name='criar_patrimonio'),
    path('patrimonios/<int:id>/editar/', views.editar_patrimonio, name='editar_patrimonio'),
    path('patrimonios/<int:pk>/excluir/', views.excluir_patrimonio, name='excluir_patrimonio'),
    path('emprestimos/', views.listar_emprestimos, name='listar_emprestimos'),
    path('emprestimos/novo/', views.criar_emprestimo, name='criar_emprestimo'),
    path('emprestimos/<int:id>/editar/', views.editar_emprestimo, name='editar_emprestimo'),
    path('emprestimos/<int:pk>/excluir/', views.excluir_emprestimo, name='excluir_emprestimo'),
    path('inventarios/', views.listar_inventarios, name='listar_inventarios'),
    path('inventarios/novo/', views.criar_inventario, name='criar_inventario'),
    path('inventarios/<int:id>/editar/', views.editar_inventario, name='editar_inventario'),
    path('inventarios/<int:pk>/excluir/', views.excluir_inventario, name='excluir_inventario'),
    # path('inventarios/', views.listar_inventarios, name='listar_inventarios'),
    # path('emprestimos/', views.listar_emprestimos, name='listar_emprestimos'),
]