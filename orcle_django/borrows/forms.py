from django import forms
from django.forms import ModelForm
from models import Item

# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['nome, autor, descricao, dono, tipo, foto, status']

# class ItemCreate(CreateView):
#     model = Item
#     fields = ['nome, autor, descricao, dono, tipo, foto, status']

# class ItemUpdate(UpdateView):
#     model = Item
#     fields = ['nome, autor, descricao, dono, tipo, foto, status']


# class ItemDelete(DeleteView):
#     model = Item
#     success_url = reverse_lazy('itens')    


