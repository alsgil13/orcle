from django.shortcuts import render
from borrows.models import TipoItem, Item, Profile, Emprestimo

def index(request):
    """Página Inicial do site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')