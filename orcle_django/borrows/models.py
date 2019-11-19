from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tipo_de_Item(models.Model):
    nome = models.CharField(max_length=200, help_text='Digite o nome tipo de objeto')
    descricao = models.TextField(max_length=1000, help_text='Insirta uma breve descrição do objeto')

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, primary_key=True)
    dt_nasc = models.DateField()
    cep = models.CharField(max_length=8, help_text='Digite o CEp do seu endereço')
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)
    pais = models.CharField(max_length=50)
    foto = models.ImageField(upload_to = 'profile_pics/', default = 'profile_pics/no-image-icon.png')
    
class Item(models.Model):
    nome = models.CharField(max_length=200, help_text='Digite o nome do objeto')
    autor = models.CharField(max_length=200, help_text='Digite o nome do autor, cantor, banda, criador, marca etc...')
    descricao = models.TextField(max_length=1000, help_text='Insirta uma breve descrição do objeto')
    dono = models.ForeignKey('Profile', on_delete=models.CASCADE)
    tipo = models.ForeignKey('Tipo_de_Item', on_delete=models.SET_NULL, null=True)
    foto = models.ImageField(upload_to = 'item_pics/', default = 'item_pics/no-image-icon.png')
    LOAN_STATUS = (
        ('e', 'Emprestado'),
        ('i', 'Indisponível'),
        ('d', 'Disponível'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        default='d',
        help_text='Status do item',
    )
    dtCadastro = models.DateTimeField(auto_now_add=True)




class Emprestimo(models.Model):
    dtEmprestimo = models.DateField()
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    pessoa = models.ForeignKey('Profile', on_delete=models.CASCADE)
    dtDevolucao = models.DateField()
    aberto = models.BooleanField()

    class Meta:
        ordering = ['dtDevolucao']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.item.nome} ({self.pessoa.first_name} {self.pessoa.last_name})'

