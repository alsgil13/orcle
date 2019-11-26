from django.shortcuts import render, redirect
from borrows.models import TipoItem, Item, Profile, Emprestimo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic

from borrows.forms import SignUpForm

from django.contrib.auth import login, authenticate

import requests



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.dt_nasc = form.cleaned_data.get('dt_nasc')
            user.profile.cep = form.cleaned_data.get('cep')
            viacep = 'http://viacep.com.br/ws/' + str(user.profile.cep) + '/json'
            r = requests.get(viacep)
            user.profile.cidade = r.json()['localidade']
            user.profile.estado = r.json()['uf']
            user.profile.pais = 'Brasil'
            #Usar requests para pegar cidade estado e pais
            user.save()
            user.profile.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('sobre')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})




def index(request):
    """Página Inicial do site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

def sobre(request):
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'sobre.html')

# --------------- Perfil ----------------------------------


class PerfilUpdate(UpdateView):
    model = Profile
    fields = ['dt_nasc','cep','cidade','estado','pais','foto']
    success_url = reverse_lazy('itens')   


class PerfilDelete(DeleteView):
    model = Profile
    success_url = reverse_lazy('itens')    

@login_required
def perfil(request):
    usuario = Profile.objects.get(pk=request.user)
    itens = Item.objects.filter(dono=request.user)
    nome = request.user.first_name + " " + request.user.last_name
    dt_nasc = usuario.dt_nasc
    foto = usuario.foto.url
    cidade = usuario.cidade
    estado = usuario.estado
    idusr = request.user.id

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
        'cidade' : cidade,
        'estado' : estado,
        'id' : idusr,

    }

    return render(request, 'meuperfil.html', context=context)




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





#Servir arquivo

import tarfile
from io import BytesIO


# def serve_file(request):
#     out = BytesIO()
#     tar = tarfile.open(mode = "w:gz", fileobj = out)
#     data = 'lala'.encode('utf-8')
#     file = BytesIO(data)
#     info = tarfile.TarInfo(name="1.txt")
#     info.size = len(data)
#     tar.addfile(tarinfo=info, fileobj=file)
#     tar.close()

#     response = HttpResponse(out.getvalue(), content_type='application/tgz')
#     response['Content-Disposition'] = 'attachment; filename=myfile.tgz'
#     return response