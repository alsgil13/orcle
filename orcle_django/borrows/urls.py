from django.urls import path
from borrows import views


urlpatterns = [
    path('', views.index, name='index'),
    path('itens/', views.ItemListView.as_view(), name='itens'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('pessoas/', views.PessoaListView.as_view(), name='pessoas'),
    path('pessoa/<int:pk>', views.PessoaDetailView.as_view(), name='pessoa-detail'),    
    path('sobre', views.sobre, name='sobre'),

]