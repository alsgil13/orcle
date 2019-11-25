from django.conf.urls import url
from orcle_app import views

urlpatterns=[
    url(r'^$', views.index,name='index')
]