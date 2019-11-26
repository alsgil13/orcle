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
    paginate_by = 3 

class TipoItemListView(LoginRequiredMixin, generic.ListView):
    model = TipoItem
    paginate_by = 4  

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
# --------------- Item ----------------------------------
class ItemCreate(CreateView):
    model = Item
    fields = ['nome', 'autor', 'descricao', 'tipo', 'foto', 'status']
    success_url = reverse_lazy('itens')   

    def form_valid(self, form):
        form.instance.dono = self.request.user
        return super().form_valid(form)

class ItemUpdate(UpdateView):
    model = Item
    fields = ['nome', 'autor', 'descricao', 'tipo', 'foto', 'status']
    success_url = reverse_lazy('itens')   


class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('itens')    

# --------------- TipoItem ----------------------------------

class TipoItemCreate(CreateView):
    model = TipoItem
    fields = '__all__'
    success_url = reverse_lazy('itens')   

class TipoItemUpdate(UpdateView):
    model = TipoItem
    fields = '__all__'
    success_url = reverse_lazy('itens')   


class TipoItemDelete(DeleteView):
    model = TipoItem
    success_url = reverse_lazy('itens')    

