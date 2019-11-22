from django.urls import path
from borrows import views


urlpatterns = [
    path('', views.index, name='index'),
    path('itens/', views.ItemListView.as_view(), name='itens'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail')

]