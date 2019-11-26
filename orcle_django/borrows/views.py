from django.shortcuts import render
from borrows.models import TipoItem, Item, Profile, Emprestimo
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    """Página Inicial do site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

def sobre(request):
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'sobre.html')

from django.views import generic

@login_required
def perfil(request):
    usuario = Profile.objects.get(pk=request.user)
    itens = Item.objects.filter(dono=request.user)
    nome = request.user.first_name + " " + request.user.last_name
    dt_nasc = usuario.dt_nasc
    foto = usuario.foto.url

    listaitens = []
    for i in itens:
        dados = {
            'item': i
        }
        listaitens.append(i)
    #Criar Contexto
    context = {
        'nome'   : nome,
        'dt_nasc' : dt_nasc,
        'foto' : foto,
        'itens' : listaitens,
    }

    return render(request, 'meuperfil.html', context=context)


from django.views import generic

class MeusItensListView(LoginRequiredMixin, generic.ListView):
    model = Item   
    paginate_by = 3
    def get_queryset(self):
        return Item.objects.filter(dono=self.request.user)
    template_name = 'borrows/meusitens_list.html'


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

