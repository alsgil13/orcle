from django.shortcuts import render
from borrows.models import TipoItem, Item, Profile, Emprestimo

from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    """Página Inicial do site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

def sobre(request):
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'sobre.html')

from django.views import generic


class ItemListView(LoginRequiredMixin, generic.ListView):
    model = Item    

class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    model = Item    

class PessoaListView(LoginRequiredMixin, generic.ListView):
    model = Profile    

class PessoaDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile        

# class PerfilDetailView(generic.DetailView):
#     model = Profile         


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# class CadastraItem(ModelForm):
#     class Meta:
#         model = Item
#         fields = ['nome, autor, descricao, dono, tipo, foto, status']


# CRUD Genérico do Django
class ItemCreate(CreateView):
    model = Item
    fields = ['nome', 'autor', 'descricao', 'tipo', 'foto', 'status']
    success_url = reverse_lazy('itens')   
    # def get_usuario(self, form):
    #     form.instance.user = self.request.user
    #     return form.instance.user
    def form_valid(self, form):
        form.instance.dono = self.request.user
        #initial = {'dono':form.instance.created_by}
        return super().form_valid(form)




class ItemUpdate(UpdateView):
    model = Item
    fields = ['nome', 'autor', 'descricao', 'tipo', 'foto', 'status']
    success_url = reverse_lazy('itens')   


class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('itens')    
