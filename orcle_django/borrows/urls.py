from django.urls import path
from borrows import views


urlpatterns = [
    path('', views.index, name='index'),
]