from django.shortcuts import render
from borrows.models import TipoItem, Item, Profile, Emprestimo

def index(request):
    """Página Inicial do site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

from django.views import generic


class ItemListView(generic.ListView):
    model = Item    

class ItemDetailView(generic.DetailView):
    model = Item    